from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home')
]