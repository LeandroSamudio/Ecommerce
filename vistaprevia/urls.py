from django.urls import path
from vistaprevia import views
from vistaprevia.views import Templatetags1

urlpatterns = [
    path('', views.index, name='index'),
    path('templatetags1', Templatetags1.as_view(), name='templatetags1'),
    path('catalog', views.catalog, name='catalog'),
    path('contacto', views.contacto, name='contacto'),
    path('imprimitumodelo', views.imprimitumodelo, name='imprimitumodelo'),
]