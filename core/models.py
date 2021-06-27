from django.db import models
import uuid
# Create your models here.
class NoticiaOtrasFuentes(models.Model):
    idnoticia=models.UUIDField(verbose_name="id", default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    fuente=models.URLField(verbose_name="fuente", max_length=400)
    def __str__(self):
        return self.titulo
class NoticiaDeportes(models.Model):
    idnoticia=models.UUIDField(verbose_name="id", default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    info=models.TextField(verbose_name="info")
    def __str__(self):
        return self.titulo
class NoticiaPoliticas(models.Model):
    idnoticia=models.UUIDField(verbose_name="id", default=uuid.uuid4)
    titulo=models.CharField(max_length=80, verbose_name="titulo")
    imagen = models.ImageField(verbose_name="imagen",upload_to="media")
    info=models.TextField(verbose_name="info")
    def __str__(self):
        return self.titulo