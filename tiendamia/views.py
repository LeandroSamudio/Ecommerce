from django.shortcuts import render
from productos.models import Producto
from tienda.forms import CargarForm
from django.shortcuts import redirect

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

