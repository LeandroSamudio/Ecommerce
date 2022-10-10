import pytest
from vistaprevia.models import Categoria
from vistaprevia.models import Producto
from django.contrib.auth.models import User
import datetime
from faker import Faker

fake = Faker()
from pytest_factoryboy import register
from tests.vistaprevia.factories import CategoriaFactory
from tests.vistaprevia.factories import ProductoFactory

register(CategoriaFactory)
register(ProductoFactory)


@pytest.fixture()
def crear_producto(db):
    mi_producto = Producto(
        producto="Producto 4", fecha_publicacion=datetime.datetime.now()
    )
    mi_producto.save()

    return mi_producto


@pytest.fixture()
def crear_producto_factory(db):
    categoria1 = Categoria(nombre="Cat1", slug="cat1")
    categoria1.save()

    def crear_producto(
        estado: str = "Borrador",
        producto: str = "Producto 1",
        fecha_publicacion=datetime.datetime.now(),
        imagen: str = "ruta",
        categoria=categoria1,
    ):
        mi_producto = Producto(
            estado=estado,
            producto=producto,
            fecha_publicacion=fecha_publicacion,
            imagen=imagen,
            categoria=categoria,
        )
        mi_producto.save()
        return mi_producto

    return crear_producto


@pytest.fixture()
def producto(db, crear_producto_factory):
    return crear_producto_factory(
        "Borrador", fake.name(), fake.date(), fake.file_path()
    )
