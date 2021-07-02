from django.urls import path,include,re_path
from .views import index,noticias,crearColaborador,form_eliminar,form_modificar,DetalleNoticiaView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('',index, name='Index'),
    path('noticias',noticias, name='noticias'),
    path('crear_colaborador', crearColaborador, name="colaborador"),
    path('form_eliminar/<id>',form_eliminar, name='eliminar'),
    path('form_modificar/<id>', form_modificar, name='modificar'),
    path('noticia-detail/<str:pk>', DetalleNoticiaView.as_view(), name='noticia-detail'),

]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)