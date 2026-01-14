"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# This is the content for urls.py
from django.urls import path
from apps.views import (
    home, badiiy_kitoblar, tarixiy_kitoblar, fantastik_kitoblar, 
    ensiklopediyalar, badiiy_kitoblar_haqida, tarixiy_kitoblar_haqida, 
    fantastik_kitoblar_haqida, ensiklopediyalar_haqida
)

urlpatterns = [
    path('', home, name='home'),
    path('badiiy-kitoblar/', badiiy_kitoblar, name='badiiy_kitoblar'),
    path('tarixiy-kitoblar/', tarixiy_kitoblar, name='tarixiy_kitoblar'),
    path('fantastik-kitoblar/', fantastik_kitoblar, name='fantastik_kitoblar'),
    path('ensiklopediyalar/', ensiklopediyalar, name='ensiklopediyalar'),
    path('badiiy-kitoblar-haqida/', badiiy_kitoblar_haqida, name='badiiy_kitoblar_haqida'),
    path('tarixiy-kitoblar-haqida/', tarixiy_kitoblar_haqida, name='tarixiy_kitoblar_haqida'),
    path('fantastik-kitoblar-haqida/', fantastik_kitoblar_haqida, name='fantastik_kitoblar_haqida'),
    path('ensiklopediyalar-haqida/', ensiklopediyalar_haqida, name='ensiklopediyalar_haqida'),
]