from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from productos.models import Producto

from django.views.generic import View
import datetime

from django.shortcuts import redirect
"""
def index(request):
    return HttpResponse("Hola Mundo!")
"""
def index(request):
    params = {}
    producto = Producto.objects.all
    params['producto']=producto
    params['nombre_sitio'] = 'Libros Online'
    return render(request, 'vistaprevia/index.html', params)


def catalog(request):
    params={}
    producto = Producto.objects.filter(
            Q(estado="En Stock")
        )
    params["los_productos"]=producto
    return render(request, "vistaprevia/catalog.html", params)

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
        producto = Producto.objects.filter(
            Q(estado="En Stock")
        )
        params["los_productos"]=producto


        params["fecha_de_hoy"]=datetime.datetime.now()
        params["mi_lista"]=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        params["row3"]="row3"
        params["mi_lista2"]=[]

        return render(request, self.template, params)

    def post(self, request):
        params={}
        producto=request.POST.get("producto")
        el_pedido = request.session.get("el_pedido")
        if el_pedido:
            cantidad = el_pedido.get(producto)
            if cantidad:
                el_pedido[producto]=cantidad+1
            else:
                el_pedido[producto]=1
        else:
            el_pedido={}
            el_pedido[producto]=1

        request.session["el_pedido"]=el_pedido
        print(request.session["el_pedido"])

        return redirect("templatetags1")



