"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse
from app import views


# todas as urls

urlpatterns = [
    path('', views.index, name="home"),
    path('estagios/', views.estagios, name="estagios"),
    path('cursos/',views.cursos, name="cursos"),
    path('como_ingressar/', views.como_ingressar, name="como_ingressar"),
    path('galeria/', views.galeria, name = "galeria"),
    path('contato/', views.contato, name="contato"),
    path('about/', views.about, name="about"),


    path('admin/', admin.site.urls),
]
