from multiprocessing import Event
from django.shortcuts import render
from django.shortcuts import  HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import Receta, Ingrediente


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
        return all_events(request)

def all_events(request):
    
    colorModo = request.GET.get("modo")
    if colorModo is not None:
        if request.session["fav_color"] == "white":
            request.session["fav_color"] = "black"
        else:
            request.session["fav_color"] = "white"

    query = request.GET.get("busqueda")
    if query is not None:
        object_list = Receta.objects.filter(nombre__contains=query)
        if not object_list:
            recetas_list = Receta.objects.all()
            context = {
                'resultado': recetas_list,
            }
        else:
            context = {
                'resultado': object_list,
            }
    else:
        recetas_list = Receta.objects.all()
        context = {
            'resultado': recetas_list,
        }
    
    
    
    return render(request, 'base.html', context)