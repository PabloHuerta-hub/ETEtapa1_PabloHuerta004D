from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import CategoriaNoticia,NoticiasPagina
class noticiaForm(forms.ModelForm):
    class Meta:
        model=NoticiasPagina
        fields=['titulo','categoria','imagen','urls','info']
        imagen=forms.FileField()
        labels={

            'titulo':'Titulo',
            'categoria':'Categoria',
            'imagen':'Imagen',
            'urls':'URLS',
            'info':'Info',
        }
        widgets={
            'titulo':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese titulo de noticia',
                    'id':'titulo'
                }
            ),
            'categoria':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'categoria'
                }
            ),
            'urls':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese link de video',
                    'id':'urls'
                }
            ),
            'info':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese informacion de la noticia',
                    'id':'info'
                }
            )

        }