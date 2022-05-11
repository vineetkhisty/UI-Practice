from django.db import models
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
    
    #Now execute python manage.py makemigrations. This will show No changes detected.

    # So to solve this u need to register the model and for that go to admin.py

    #After doing the required settings, run 
    # 1. python manage.py makemigrations
    # 2. python manage.py migrate