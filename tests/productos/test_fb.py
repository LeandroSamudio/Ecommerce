import pytest
from productos.models import Producto
from django.contrib.auth.models import User
import datetime

def test_nuevo_producto(db, producto_factory):
    #print(producto_factory.producto)
    producto = producto_factory.create()
    print(producto.producto)
    assert True
