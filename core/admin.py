from django.contrib import admin
from .models import NoticiaOtrasFuentes,NoticiaDeportes,NoticiaPoliticas
# Register your models here.
admin.site.register(NoticiaOtrasFuentes)
admin.site.register(NoticiaDeportes)
admin.site.register(NoticiaPoliticas)