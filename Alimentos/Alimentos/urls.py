"""Alimentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from customer.views import Index, About,Restruantdisplay,AreaandFood
from appmanager.views import Admin,Addcity,Del,Deleted,Added

urlpatterns = [
    path('',Index.as_view(),name = 'index'),
    path('areaandfood/',AreaandFood.as_view(),name='areaandfood'),
    path('about/',About.as_view(),name = 'about'),
    path('restraunt/',Restruantdisplay.as_view(),name = 'restraunt'),
    path('addcity/',Addcity.as_view(),name = 'addcity'),
    path('administrator/',Admin.as_view(),name = 'administrator'),
    path('Del/',Del.as_view(),name = 'Delete'),
    path('Deleted/',Deleted.as_view(),name = 'deleted'),
    path('Added/',Added.as_view(),name="added"),
    
] 
