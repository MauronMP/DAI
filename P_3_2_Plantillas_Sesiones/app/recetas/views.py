from multiprocessing import Event
from django.shortcuts import render
from django.shortcuts import  HttpResponse

from .models import Receta


def index(request):
    return render(request, "base.html")

def all_events(request):
    recetas_list = Receta.objects.all()
    return render(request, 'base.html', {'recetas_list' : recetas_list})