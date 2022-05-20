from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='main'),
    path("home",views.home,name='home'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("profile",views.profile,name='profile'),
    path("resetpassword",views.resetpassword,name='resetpassword'),
    path("password_reset_done",views.password_reset_done,name='password_reset_done'),
    path('about',views.about,name='about'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact us')
    

]