import email
from unicodedata import name
from django import template
from django.shortcuts import render, HttpResponse
from datetime import datetime

# from sympy import re
from home.models import Contact, Register
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render_to_response
# from django.template import RequestContext


# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('This is home page')


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('This is home page')


def about(request):
    return render(request, 'about.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    if request.method == "POST":

        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        subject1 = request.POST.get('subject')
        message1 = request.POST.get('message')
        contact = Contact(name=name1, email=email1, subject=subject1,
                          message=message1, date=datetime.today())
        contact.save()
        messages.success(request, 'Your detail have been sent!')
    return render(request, 'contact.html')


def register(request):
    if request.method == "POST":

        name2 = request.POST.get('name')
        email2 = request.POST.get('email')
        password2 = request.POST.get('password')
        print('Name', name2)
        register = Register(name1=name2, email1=email2,
                            password1=password2, date1=datetime.today())
        register.save()
        messages.success(request, 'You are successfully registered!')
    return render(request, 'index.html')


def login(request):

    # fm = AuthenticationForm()
    # return render(request,"index.html",{'form':fm})
    if request.method == "POST":
       username = request.POST.get('email')
       password = request.POST.get('password')
       registerentry = Register.objects.all()
       print(type(registerentry))
       for regdata in registerentry.iterator():
            if username == regdata.email1:
                if regdata.password1 == password:
                    Name = regdata.name1
                    # print(Name)
                    messages.success(request, 'Login Successful!Welcome,'+ regdata.name1)
                    profile(request,Name)
                    # return render(request, 'home.html')
                    context = {'Name': Name}
                    return render(request,'home.html',context)
            
                else:
                    messages.error(request,"Invalid username or password!")
                    return render(request, 'index.html')
    

def resetpassword(request):
    return render(request, 'resetpassword.html')


def password_reset_done(request):
    if request.method == "POST":
        email = request.POST.get('email')
        newpassword =request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        registerentry = Register.objects.get(email1=email)
        if registerentry is not None:
            if email == registerentry.email1:
                if registerentry.password1 == newpassword:
                    messages.error(request, 'old and new password are same please choose a new one')
                    return render(request, 'resetpassword.html')
                    
                else:
                    if confirmpassword == newpassword:
                        registerentry.password1 = newpassword
                        registerentry.save()
                        messages.info(request,"Your password has been changed successfully!")
                        return render(request, 'password_reset_done.html')
                    else:
                        messages.error(request, 'Passwords does not match')
                        return render(request, 'resetpassword.html')
        else:
            messages.error(request, 'Email does not match')
            return render(request, 'resetpassword.html')
        # return render(request, 'password_reset_done.html')

def profile(request,Name1):
    Name = Name1
    print("profile Name:",Name)
    context = { 'Name': Name}
    return HttpResponse(template.render(context,request))
    # return render(request,'profile.html',context)