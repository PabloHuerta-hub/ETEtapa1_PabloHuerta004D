from django.db import models
import uuid
from django.urls import reverse
# Create your models here.
class CategoriaNoticia(models.Model):
    idCategoria = models.UUIDField(primary_key=True, verbose_name='Id de Categoria', default=uuid.uuid4)
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoría')
    def __str__(self):
        return self.nombreCategoria

class NoticiaOtrasFuentes(models.Model):
    idnoticia=models.UUIDField(primary_key=True,verbose_name="id", default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    fuente=models.URLField(verbose_name="fuente", max_length=400)
    def __str__(self):
        return self.titulo
class NoticiaDeportes(models.Model):
    idnoticia=models.UUIDField(primary_key=True,verbose_name="id", default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    info=models.TextField(verbose_name="info")
    def __str__(self):
        return self.titulo
class NoticiaPoliticas(models.Model):
    idnoticia=models.UUIDField(primary_key=True,verbose_name="id", default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    info=models.TextField(verbose_name="info")
    def __str__(self):
        return self.titulo

class NoticiasPagina(models.Model):
    idnoticia=models.UUIDField(primary_key=True,verbose_name="id",default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    categoria=models.ForeignKey(CategoriaNoticia,on_delete=models.CASCADE,related_name="TipoNoticias")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    urls=models.URLField(verbose_name="url",max_length=200)
    info=models.TextField(verbose_name="info")
    class Meta:
        ordering=['titulo']
    def __str__(self):
        return self.titulo

class Colaborador(models.Model):
    rut=models.CharField(max_length=100, verbose_name="rut", primary_key=True)
    foto=models.ImageField(verbose_name="imagen",upload_to="media")
    nombre= models.CharField(max_length=200, verbose_name="nombre")
    telefono=models.IntegerField(verbose_name="telefono")
    direccion=models.CharField(verbose_name="direccion", max_length=100)
    email=models.CharField(verbose_name="email", max_length=200)
    pais=models.CharField(verbose_name="pais", max_length=80)
    contra=models.CharField(verbose_name="pass", max_length=200,blank=True,null=True)
    def __str__(self):
        return self.nombre