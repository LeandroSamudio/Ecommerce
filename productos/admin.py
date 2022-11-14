from django.contrib import admin
from productos.models import Categoria
from productos.models import Producto
from django.http import HttpResponse
from django.core import serializers


admin.site.site_header= "Templo 3D Admin"
admin.site.site_title= "Tempro 3D Admin"
admin.site.index_title= "Bienvenido al portal de administracion"
class ProductoInline(admin.TabularInline):

    model = Producto
    extra = 0

class CategoriaAdmin(admin.ModelAdmin):
    inlines = [ProductoInline]





@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    #fields =['categoria', 'fecha_publicacion', 'producto', 'imagen']

    fieldsets = [
        ("Relación", {"fields": ["categoria"]}),
        (
            "Datos generales",
            {
                "fields": [
                    'fecha_publicacion', 'producto', 'estado' , 'imagen', 'descripcion'
                ]
            },
        ),
        (
            "Datos economicos",
            {
                "fields": [
                    'precio', 'stock', 'descuento'
                ]
            },
        ),

    ]
    actions=["publicar", "borrador", "retirado", "exportar_a_json"]
    list_display = ['producto', 'fecha_publicacion', 'tipo_de_estado', 'imagen', 'precio']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion',)
    search_fields=('producto', 'estado',)
    list_display_links = ('producto', 'fecha_publicacion',)






    def publicar(self, request, queryset):
        registro = queryset.update(estado=Producto.Borrador)

        if registro == 1:
            mensaje = "1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)


    publicar.short_description = "Pasar a publicado"



    def borrador(self, request, queryset):
        registro = queryset.update(estado=Producto.Publicado)

        if registro == 1:
            mensaje = "1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)


    borrador.short_description = "publicar sin stock"



    def retirado(self, request, queryset):
        registro = queryset.update(estado=Producto.Retirado)

        if registro == 1:
            mensaje = "1 registro actualizado"
        else:
            mensaje = "%s registros actualizados" % registro
        self.message_user(request, "%s exitosamente" % mensaje)


    retirado.short_description = "Sacar de publicado"






    def exportar_a_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response




    @admin.display(description='Name')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.producto, obj.estado)).upper()

#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)


#admin.site.register(Categoria)
#admin.site.register(Producto)

