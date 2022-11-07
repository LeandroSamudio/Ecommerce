from django.shortcuts import render

def pagina_logout(request):
    params={}
    return render(request, "usuarios/logout.html", params)