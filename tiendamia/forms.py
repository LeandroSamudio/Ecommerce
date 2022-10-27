from dataclasses import field
from itertools import product
from django.forms import ModelForm
from productos.models import Producto

class CargarForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'fecha_publicacion', 'imagen']

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)