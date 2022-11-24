from multiprocessing import Event
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Receta, Ingrediente
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Receta
from django.contrib import messages

def post_detail(request, pk):
    post = get_object_or_404(Receta, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.info(request, "Se ha creado la receta")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request,'post_edit.html', {'form': form})

def update_recipe(request, pk):
    post = get_object_or_404(Receta, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.info(request, "Se ha actualizado la receta")
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})
    
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
    
    if 'fav_color' in request.session:
        colorModo = request.GET.get("modo")
        if colorModo is not None:
            if request.session["fav_color"] == "white":
                request.session["fav_color"] = "black"
            else:
                request.session["fav_color"] = "white"
    else:
        request.session["fav_color"] = "white"
    

    query = request.GET.get("busqueda")
    encontrado = request.GET.get('textbox1')
    if request.GET.get('textbox1'):
        Receta.objects.filter(id=(Receta.objects.get(nombre=encontrado)).id).delete()
        messages.info(request, "Se ha borrado la receta")
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


