from multiprocessing import Event
from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Receta, Ingrediente


def index(request):
    busqueda = request.GET.get('busqueda')
    print(busqueda)
    return render(request, "base.html")


def buscar(request):
    
    data= request.POST.get('textbox1')
    if data is not None:
        Receta_1 = Receta.objects.get(nombre__contains=data)
        Ingredientes_1 = Ingrediente.objects.filter(receta=Receta_1)
        
        context = {
            'receta': Receta_1,
            'ingrediente': Ingredientes_1,
        }
        return render(request, 'buscar.html', context)
    else:
        return render(request, "buscar.html")


def all_events(request):
    recetas_list = Receta.objects.all()
    context = {
        'resultado': recetas_list,
    }
    return render(request, 'base.html', context)