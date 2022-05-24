from tkinter import CASCADE
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Role(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    firstName = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=30)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" %(self.firstName, self.lastName)


    #Now go to admin.py and register your models