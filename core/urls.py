from django.urls import path,include,re_path
from .views import index,noticias,MovieDetailView,crearNoticia
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path('',index, name='Index'),
    path('noticias',noticias, name='Noticias'),
    path('crear_noticia', crearNoticia, name="crearNoticia"),
    path('noticias/<str:pk>', MovieDetailView.as_view(), name='movie-detail'),
]
if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)