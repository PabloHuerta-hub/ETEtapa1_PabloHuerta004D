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
    titulo=models.CharField(primary_key=True,max_length=80, verbose_name="titulo")
    categoria=models.ForeignKey(CategoriaNoticia,on_delete=models.CASCADE,related_name="TipoNoticias")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    urls=models.URLField(verbose_name="url",max_length=200)
    info=models.TextField(verbose_name="info")
    class Meta:
        ordering=['titulo']
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('movie-detail', args=[str(self.titulo)])