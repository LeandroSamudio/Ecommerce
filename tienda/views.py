from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from productos.models import Producto
from tienda.forms import CargarForm
from django.http import Http404
from django.views.generic import View

def cargar_imagen(request):
    params={}
    if request.method == 'POST':
        form = CargarForm(request.POST, request.FILES)
        params['form'] = form
        if form.is_valid():
            producto = form.cleaned_data['producto']
            fecha_publicacion = form.cleaned_data['fecha_publicacion']
            imagen = form.cleaned_data['imagen']

            nuevo_producto= Producto(producto=producto, fecha_publicacion=fecha_publicacion, imagen=imagen)
            nuevo_producto.save()
            return redirect('index')
            

    
    else:
        form = CargarForm()
        params['form'] = form
        return render(request, 'tienda/formulario.html', params) 

class VerImagenes(View): 
    template = "tienda/verimagenes.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        
        return render(request, self.template, params)


def ver_imagen(request, producto_id):
    params={}
    try:
        producto = Producto.objects.get(pk=producto_id)
    except Producto.DoesNotExist:
        raise Http404
    params["producto"] = producto
    
    return render(request, "tienda/verimagen.html", params)


class EjemploLocalSotage(View): 
    template = "tienda/localstorage.html"

    def get(self, request):
        params={}
        try:
            productos = Producto.objects.all()
        except Producto.DoesNotExist:
            raise Http404
        params["productos"] = productos
        # ##########################################################
        # PARA INICIALIZAR LA VARIABLE DE SESSION CARRO
        # ###########################################################
        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}
            
        return render(request, self.template, params)