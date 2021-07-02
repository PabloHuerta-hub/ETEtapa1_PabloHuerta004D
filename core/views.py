from django.shortcuts import render, redirect, get_object_or_404
from .models import NoticiaOtrasFuentes,NoticiaDeportes,NoticiaPoliticas,NoticiasPagina,Colaborador
from .forms import Colaboradorform,noticiaForm
# Create your views here.
def index(request):
    Politica=NoticiaPoliticas.objects.all()
    Noticias=NoticiaOtrasFuentes.objects.all()
    Deportes=NoticiaDeportes.objects.all()
    return render(request,'Index.html', context={'noticias':Noticias , 'deportes':Deportes , 'politica':Politica})
def noticias(request):
    Noticias=NoticiasPagina.objects.all()
    return render(request,'Noticias.html',context={'noticias':Noticias},)

def crearColaborador(request):
    if request.method == "POST":
        formulario = Colaboradorform(request.POST or None,request.FILES or None)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('Index')
    else:
        formulario = Colaboradorform()
    return render(request, 'noticias/form_crearcolaborador.html', {'colaborador': formulario})

def form_eliminar(request,id):
    noticias = NoticiasPagina.objects.get(idnoticia=id)
    noticias.delete()
    return redirect('noticias')
def form_modificar(request, id):
    post = get_object_or_404(NoticiasPagina, idnoticia=id)
    if request.method == "POST":
        formulario = noticiaForm(request.POST, request.FILES, instance=post)
        if formulario.is_valid():
            post = formulario.save(commit=False)
            post.save()
            return redirect('noticias')
    else:
        formulario = noticiaForm(instance=post)
    return render(request, 'noticias/form_modificar.html', {'form': formulario})
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
class DetalleNoticiaView(generic.DetailView):
    model = NoticiasPagina