# Generated by Django 3.2.3 on 2021-06-28 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticiaspagina',
            name='idnoticia',
        ),
        migrations.AlterField(
            model_name='noticiaspagina',
            name='titulo',
            field=models.CharField(max_length=80, primary_key=True, serialize=False, verbose_name='titulo'),
        ),
    ]
