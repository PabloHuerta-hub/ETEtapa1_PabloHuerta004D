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

def colaborador(request):
    colaborador=Colaborador.objects.all()
    return render(request,'Colaboradores.html',context={'colaborador':colaborador})

def crearNoticias(request):
    if request.method == "POST":
        formulario=noticiaForm(request.POST or None, request.FILES or None)
        if formulario.is_valid():
            post=formulario.save(commit=False)
            post.save()
            return redirect('noticias')
    else:
        formulario=noticiaForm()
    return render(request, 'noticias/formulario_noticias.html',{'noticia':formulario})
def crearColaborador(request):
    if request.method == "POST":
        formulario = Colaboradorform(request.POST or None,request.FILES or None)
        if formulario.is_valid():
            contrasena = (formulario.cleaned_data['rut'])[0:2] + ((formulario.cleaned_data['nombre'])[0:2]).upper() + ((formulario.cleaned_data['pais'])[-2:]).lower() + str(formulario.cleaned_data['telefono'])[-2:]
            rutsolicitud = formulario.cleaned_data['rut']
            post = formulario.save(commit=False)
            post.save()
            creacontrasena = Colaborador.objects.get(rut=rutsolicitud)
            creacontrasena.contra = contrasena
            creacontrasena.save()

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
    
def Noticia_detail(request, id):
    Noticia = NoticiasPagina.objects.get(idnoticia=id)
    return render(request, 'noticias/noticia_detail.html',{'noti':Noticia})