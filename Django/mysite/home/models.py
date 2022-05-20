from django.db import models
from django.contrib.auth.models import User
# from sympy import Max

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    subject= models.CharField(max_length=122)
    message= models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Register(models.Model):

    name1= models.CharField(max_length=122)
    email1= models.CharField(max_length=122)
    password1= models.CharField(max_length=122)
    date1=models.DateField()

    def __str__(self):
        return self.name1

class UserProfile(models.Model):
	profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_img = models.ImageField(default='images/default.png')

    #Now execute python manage.py makemigrations. This will show No changes detected.

    # So to solve this u need to register the model and for that go to admin.py

    #After doing the required settings, run 
    # 1. python manage.py makemigrations
    # 2. python manage.py migrate