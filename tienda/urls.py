from django.urls import path
from tienda.views import EjemploLocalSotage
from tienda import views
from tienda.views import VerImagenes
from tienda import views_agregar

urlpatterns = [
    path('ejemplo_localstorage/', EjemploLocalSotage.as_view(), name="tienda"),
    path('cargar/', views.cargar_imagen, name="cargar"),
    path('<int:producto_id>/ver/', views.ver_imagen, name="ver"),
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path("agregar/", views_agregar.agregar, name="agregar"),
]