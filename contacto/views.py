from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from contacto.models import Consulta
from contacto.forms import ConsultaForm

class Contacto(FormView):
    template_name= "contacto/contacto.html"
    form_class = ConsultaForm
    success_url= "mensaje_enviado"

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)


class MensajeEnviado(View):
    template='contacto/mensaje_enviado.html'

    def get(self, request):
        params = {}
        params["mensaje"] = "Datos ingresado correctamente"
        return render(request, self.template, params)


# Create your views here.
