from django.shortcuts import render

def pagina_registro(request):
    params={}
    return render(request, "usuarios/registro.html", params)