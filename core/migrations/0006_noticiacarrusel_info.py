# Generated by Django 3.2.3 on 2021-06-27 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_noticiacarrusel_fuente'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticiacarrusel',
            name='info',
            field=models.TextField(default='ayuda', verbose_name='info'),
            preserve_default=False,
        ),
    ]
