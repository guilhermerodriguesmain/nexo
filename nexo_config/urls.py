"""
Configuração de URLs para o projeto nexo_config.

A lista `urlpatterns` roteia as URLs para as views. Para mais informações, consulte:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Exemplos:
Views de função
    1. Adicione uma importação:  from my_app import views
    2. Adicione uma URL a `urlpatterns`:  path('', views.home, name='home')
Views baseadas em classe
    1. Adicione uma importação:  from other_app.views import Home
    2. Adicione uma URL a `urlpatterns`:  path('', Home.as_view(), name='home')
Incluindo outro URLconf
    1. Importe a função include(): from django.urls import include, path
    2. Adicione uma URL a `urlpatterns`:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nexo.urls'))

]
