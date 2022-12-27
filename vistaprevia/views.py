from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from productos.models import Producto

from django.views.generic import View
import datetime

from django.shortcuts import redirect

from tienda.forms import SearchProductForm
import json
from django.http import HttpResponse

def para_ajax(request):
    params={}
    search=SearchProductForm()
    params['search']=search
    return render(request, 'vistaprevia/ver_ajax.html', params)

class BuscarProducto(View):
    def get(self, request):
        if request.is_ajax:
            palabra=request.GET.get('term', '')
            print(palabra)
            libro=Producto.objects.filter(producto__icontains=palabra)
            result=[]
            for an in libro:
                data={}
                data['label']=an.producto
                result.append(data)
            data_json=json.dumps(result)
        else:
            data_json="fallo"
        mimetype="application/json"
        return HttpResponse(data_json, mimetype)

class BuscarProducto2(View):
    def get(self, request):
        if request.is_ajax:
            q = request.GET['valor']
            libro = Producto.objects.filter(producto__icontains=q)
            results = []
            for rec in libro:
                print(rec.producto)
                print(rec.estado)
                print(rec.imagen)

                data = {}
                data['producto'] = rec.producto
                data['estado'] = rec.estado
                data['ruta_imagen'] = str(rec.imagen)
                results.append(data)
            data_json = json.dumps(results)

        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)


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



