from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request,'index.html')
    # return HttpResponse('This is home page')

def about(request):
    return HttpResponse('This is about page')

def service(request):
    return HttpResponse('We have various services')

def contact(request):
    return HttpResponse('Welcome to Contact us page')
