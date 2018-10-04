from django.contrib import admin
from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('core/contato/', views.contato, name='contato'),
    path('core/artigo/', views.artigo, name='artigo'),
    path('core/lista_artigos/', views.lista_artigos, name='lista_artigos'),
    path('admin/', admin.site.urls),
]
