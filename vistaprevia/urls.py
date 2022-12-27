from django.urls import path
from vistaprevia import views
from vistaprevia.views import Templatetags1
from vistaprevia.views import BuscarProducto
from vistaprevia.views import BuscarProducto2
urlpatterns = [
    path('', views.index, name='index'),
    path('templatetags1', Templatetags1.as_view(), name='templatetags1'),
    path('catalog', views.catalog, name='catalog'),
    path('contacto', views.contacto, name='contacto'),
    path('imprimitumodelo', views.imprimitumodelo, name='imprimitumodelo'),
    path('usar_ajax', views.para_ajax, name='usar_ajax'),
    path('buscar_producto/', BuscarProducto.as_view(), name='buscar_producto'),
    path('buscar_producto2/', BuscarProducto2.as_view(), name='buscar_producto2'),
]