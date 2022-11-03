from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from productos.models import Producto

from django.views.generic import View
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

class Templatetags1(View):
    template = "vistaprevia/templatetags1.html"
    def get(self, request):
        params = {}
        return render(request, self.template, params)

    

