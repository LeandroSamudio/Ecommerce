from django.db import models
from django.utils.html import format_html

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s' % self.nombre




class Producto(models.Model):

    Borrador = 'En Stock'
    Publicado = 'Sin Stock'
    Retirado = 'Sin publicar'
    APROBACION_PRODUCTO = (
        (Borrador, 'En Stock'),
        (Publicado, 'Sin Stock'),
        (Retirado, 'Sin publicar'),
    )
    estado = models.CharField(
        max_length=15, choices=APROBACION_PRODUCTO, default='Publicado'
        )

    producto = models.CharField(max_length=200)
    precio = models.CharField(max_length=10, null=True, blank=True, default='0')
    fecha_publicacion = models.DateTimeField('Fecha de publicación')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 
    # categoria = models.ManyToManyField(Categoria)    
    categoria = models.ForeignKey(
        Categoria, blank=False, null=True, on_delete=models.CASCADE
    )

    stock = models.IntegerField(default=0)
    descripcion = models.TextField( default="")
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    descuento = models.IntegerField(default=0)

    
    def tipo_de_estado(self,):
        if self.estado == 'En Stock':
            return format_html('<span style="color: #0d0;">{}</span>', self.estado, )
        elif self.estado == 'Sin Stock':
            return format_html('<span style="color: #d00;">{}</span>', self.estado, )
        elif self.estado == 'Sin publicar':
            return format_html('<span style="color: #00d;">{}</span>', self.estado, )

    def __str__(self, ):
        return self.producto + "---" + str(self.fecha_publicacion)