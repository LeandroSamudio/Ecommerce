from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from productos.models import Producto
"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
def index(request):
    params = {}
    params['nombre_sitio'] = 'Libros Online'
    return render(request, 'vistaprevia/index.html', params)


def catalog(request):
    return render(request, "vistaprevia/catalog.html")

def contacto(request):
    return render(request, "vistaprevia/contacto.html")


def imprimitumodelo(request):
    return render(request, "vistaprevia/imprimitumodelo.html")