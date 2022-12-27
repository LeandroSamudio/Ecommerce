from dataclasses import field
from itertools import product
from django.forms import ModelForm
from productos.models import Producto
from django import forms
class SearchProductForm(forms.Form):
    querycom = forms.CharField(label='Ingresar el nombre de libro a buscar', widget=forms.TextInput(attrs={'size': 32, 'class': 'form- control'}))


class CargarForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['producto', 'fecha_publicacion', 'imagen']

        error_messages = {
            "producto": {
                "required": ("Se debe agregar un nombre de producto"),
            },
            "fecha_publicacion": {
                "required": (
                    "Se debe agregar la fecha de publicación en el formato adecuado"
                ),
            },
        }

    def __init__(self, *args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)