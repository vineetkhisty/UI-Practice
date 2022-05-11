import email
from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact,Register
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')
    # return HttpResponse('This is home page')

def home(request):
    return render(request,'home.html')
    # return HttpResponse('This is home page')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method =="POST":

        name1 =request.POST.get('name')
        email1 = request.POST.get('email')
        subject1 = request.POST.get('subject')
        message1 = request.POST.get('message')
        contact = Contact(name= name1,email=email1,subject=subject1,message=message1,date=datetime.today())
        contact.save()
        messages.success(request, 'Your detail have been sent!')
    return render(request,'contact.html')

def register(request):
    if request.method == "POST":

        name2 = request.POST.get('name')
        email2= request.POST.get('email')
        password2=request.POST.get('password')
        print('Name',name2)
        register = Register(name1=name2,email1=email2,password1=password2,date1=datetime.today())
        register.save()
        messages.success(request,'You are successfully registered!')
    return render(request,'index.html')