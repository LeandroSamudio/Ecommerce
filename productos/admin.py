from django.contrib import admin
from productos.models import Categoria
from productos.models import Producto



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
                    'fecha_publicacion', 'producto', 'estado' , 'imagen', 'precio'
                ]
            },
        ),

    ]
    list_display = ['producto', 'fecha_publicacion', 'tipo_de_producto', 'imagen', 'precio']
    ordering = ['-fecha_publicacion']
    list_filter = ('producto', 'fecha_publicacion',)
    search_fields=('producto', 'estado',)
    list_display_links = ('producto', 'fecha_publicacion',)

    @admin.display(description='Name')
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.producto, obj.estado)).upper()

#admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)


#admin.site.register(Categoria)
#admin.site.register(Producto)
