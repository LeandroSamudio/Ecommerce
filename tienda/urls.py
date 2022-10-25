from django.urls import path
from tienda import views
from tienda.views import VerImagenes

urlpatterns = [
    path('cargar/', views.carga_imagen, name="cargar"),
    path('<int:producto_id>/ver/', views.ver_imagen, name="ver"),
    path('verimagenes/', VerImagenes.as_view8, name="verimagenes"),
]