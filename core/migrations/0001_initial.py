# Generated by Django 3.2.3 on 2021-06-28 04:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaNoticia',
            fields=[
                ('idCategoria', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='NoticiaDeportes',
            fields=[
                ('idnoticia', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=80, verbose_name='titulo')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='imagen')),
                ('info', models.TextField(verbose_name='info')),
            ],
        ),
        migrations.CreateModel(
            name='NoticiaOtrasFuentes',
            fields=[
                ('idnoticia', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=80, verbose_name='titulo')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='imagen')),
                ('fuente', models.URLField(max_length=400, verbose_name='fuente')),
            ],
        ),
        migrations.CreateModel(
            name='NoticiaPoliticas',
            fields=[
                ('idnoticia', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=80, verbose_name='titulo')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='imagen')),
                ('info', models.TextField(verbose_name='info')),
            ],
        ),
        migrations.CreateModel(
            name='NoticiasPagina',
            fields=[
                ('idnoticia', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=80, verbose_name='titulo')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='imagen')),
                ('urls', models.URLField(verbose_name='url')),
                ('info', models.TextField(verbose_name='info')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TipoNoticias', to='core.categorianoticia')),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
    ]
