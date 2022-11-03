from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from productos.models import Producto

from django.views.generic import View
import datetime
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
        params["cross_site_scripting"]="""
            <script>$("*").css({
                "background-color": "yellow",
                "font-weight": "bolder",
            });
            </script>
        """

        params["fecha_de_hoy"]=datetime.datetime.now()
        params["mi_lista"]=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        params["row3"]="row3"
        params["mi_lista2"]=[]

        return render(request, self.template, params)

    

