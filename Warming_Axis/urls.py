"""Warming_Axis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from noticias import views as news_views
from Warming_Axis import views as local_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('noticias/', news_views.noticias, name='noticias'),
    path('inicio/',local_views.Inicio, name="inicio"),
    path('noti/',local_views.noticias,),
    path('info/',local_views.informacion, name='info'),
    path('foros/',local_views.foros, name='foros'),
    path('acerca_de/',local_views.acerca, name='acerca'),
]