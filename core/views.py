from django.shortcuts import render, redirect, get_object_or_404
from .models import NoticiaOtrasFuentes,NoticiaDeportes,NoticiaPoliticas,NoticiasPagina
from .forms import noticiaForm
# Create your views here.
def index(request):
    Politica=NoticiaPoliticas.objects.all()
    Noticias=NoticiaOtrasFuentes.objects.all()
    Deportes=NoticiaDeportes.objects.all()
    return render(request,'Index.html', context={'noticias':Noticias , 'deportes':Deportes , 'politica':Politica})
def noticias(request):
    CategoriaD="d2c65000-7f56-4e9d-a2bb-8e6d90eee540"
    CategoriaP="a0afb980-d821-4ad4-b4de-15fc180f4012"
    CategoriaI="d2c65000-7f56-4e9d-a2bb-8e6d90eee540"
    NoticiasPolitica=NoticiasPagina.objects.all().filter(categoria=CategoriaP)
    NoticiasDeportes=NoticiasPagina.objects.all().filter(categoria=CategoriaD)
    NoticiasInternacional=NoticiasPagina.objects.all().filter(categoria=CategoriaI)
    return render(request,'Noticias.html',context={'noticiasd':NoticiasDeportes,'noticiasp':NoticiasPolitica,'noticiasi':NoticiasInternacional})
def crearNoticia(request):
    if request.method=='POST': 
        noticiaform = noticiaForm(request.POST)
        if noticiaform.is_valid():
            noticiaform.save()
            return redirect('Index')
    else:
        noticiaform= noticiaForm()
    return render(request, 'noticias/form_crearnoticia.html', {'noticiaform': noticiaform})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

class MovieDetailView(generic.DetailView):
    model = NoticiasPagina