from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Colaborador,CategoriaNoticia,NoticiasPagina
class Colaboradorform(forms.ModelForm):
    class Meta:
        model=Colaborador
        fields=['rut','foto','nombre','telefono','direccion','email','pais']
        foto = forms.ImageField(
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
        labels={

            'rut':'Rut',
            'nombre':'Nombre completo',
            'foto':'Foto',
            'telefono':'Telefono',
            'direccion':'Direccion',
            'email':'Correo',
            'pais':'Pais'
        }
        widgets={
            'rut':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su rut',
                    'id':'rut'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su nombre',
                    'id':'nombre'
                }
            ),
            'telefono':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su telefono',
                    'id':'telefono'
                }
            ),
            'direccion':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su direccion',
                    'id':'direccion'
                }
            ),
            'email':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su email',
                    'id':'email'
                }
            ),
            'pais':forms.TextInput(
                attrs={
                     'class': 'form-control',
                    'placeholder':'Ingrese su pais',
                    'id':'pais'
                }
            )

        }
class noticiaForm(forms.ModelForm):
  class Meta:
        model=NoticiasPagina
        fields=['titulo','categoria','imagen','urls','info']
        image = forms.ImageField(
            widget=forms.ClearableFileInput(
            attrs={
                'class':'form-control' 
            }
            ))
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
            ),

        }