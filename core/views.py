from django.shortcuts import render
from .models import NoticiaOtrasFuentes,NoticiaDeportes,NoticiaPoliticas
# Create your views here.
def index(request):
    Politica=NoticiaPoliticas.objects.all()
    Noticias=NoticiaOtrasFuentes.objects.all()
    Deportes=NoticiaDeportes.objects.all()
    return render(request,'Index.html', context={'noticias':Noticias , 'deportes':Deportes , 'politica':Politica})
