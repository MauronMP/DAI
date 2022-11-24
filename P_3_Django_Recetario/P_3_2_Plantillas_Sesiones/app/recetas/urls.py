# recetas/urls.py
from xml.etree.ElementInclude import include
from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.all_events, name='index'),
    path('buscar', views.buscar, name='buscar'),
]