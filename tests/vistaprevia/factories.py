import factory
from vistaprevia.models import Categoria
from vistaprevia.models import Producto
from django.contrib.auth.models import User
import datetime
from datetime import date
from faker import Faker
fake = Faker()


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria

    nombre = fake.name()
    slug = fake.name()




class ProductoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Producto

    estado = "Borrador" 
    producto = fake.name()
    fecha_publicacion = fake.date()  
    imagen = fake.file_path()
    categoria = factory.SubFactory(CategoriaFactory)