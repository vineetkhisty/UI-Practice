import email
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.


def index(request):
    return render(request,'index.html')
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

    return render(request,'contact.html')
