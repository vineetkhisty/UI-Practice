from django.contrib import admin
from django.urls import path ,include
from emp_app import views

urlpatterns = [
    path("",views.index,name='main'),
    
]
