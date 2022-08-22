from django.shortcuts import render
from django.http import HttpResponse

""""
def index(request):
    return HttpResponse("Hola Mundo!")
    # Create your views here.
"""


def index(request):
    params = {}
    params["nombre_sitio"] = "Ecommerce"
    return render(request, "vistaprevia/index.html", params)
    # Create your views here.
