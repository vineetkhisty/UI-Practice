from atexit import register
from django.contrib import admin
from home.models import Contact,Register # Import the class name present in Models.py file

# Register your models here.

admin.site.register(Contact)

admin.site.register(Register)

#After this go to apps.py, copy the name of the app, then go to installed apps

