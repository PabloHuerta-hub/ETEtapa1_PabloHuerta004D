# Generated by Django 3.2.3 on 2021-06-27 04:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_noticiacarrusel_noticiadeportes'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaPoliticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnoticia', models.UUIDField(default=uuid.uuid4, verbose_name='id')),
                ('titulo', models.CharField(max_length=80, verbose_name='titulo')),
                ('imagen', models.ImageField(upload_to='media', verbose_name='imagen')),
                ('info', models.TextField(verbose_name='info')),
            ],
        ),
    ]