# recetas/urls.py

from django.urls import path
from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.all_events, name='index'),
    path('buscar', views.buscar, name='buscar'),
    path('update_recipe/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('post_new', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]