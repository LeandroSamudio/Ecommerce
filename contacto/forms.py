from django import forms
from django.forms import ModelForm
from contacto.models import Consulta
from django import forms
from captcha.fields import CaptchaField


class ConsultaForm(ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Consulta
        fields=[
            'nombre',
            'descripcion',
            'mail',
            'telefono',
            'fecha'
            ]

    def send_email(self,):
        nombre=self.cleaned_data['nombre']
        descripcion=self.cleaned_data['descripcion']
        mail=self.cleaned_data['mail']
        telefono=self.cleaned_data['telefono']
        fecha=self.cleaned_data['fecha']

        # logica de envio de mail



