##Manually created the file
import imp

from django.shortcuts import render
# from django.contrib import renders

def index(request):
    return render(request,"index.html")