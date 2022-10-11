from django.urls import path
from vistaprevia import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog', views.catalog, name='catalog'),
    path('contacto', views.contacto, name='contacto'),
    path('imprimitumodelo', views.imprimitumodelo, name='imprimitumodelo'),
]