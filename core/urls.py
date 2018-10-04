from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='index')
    path('', views.contato, name='contato')
    path('', views.artigo, name='artigo')
    path('', views.lista_artigos, name='lista_artigos')
]
