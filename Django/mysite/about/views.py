from django import http
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to about page')