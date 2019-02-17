from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Human(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)
    Human_Type = (
        ('T', 'Teacher'),
        ('S', 'Student'),
    )
    Human_type = models.CharField(max_length=1, choices=Human_Type)

class Classroom(models.Model):
    name = models.CharField(max_length = 90, default = "class name")
    subject = models.CharField(max_length = 90, default = "class name")
    humans = models.ManyToManyField(Human)

class Task(models.Model):
    name = models.CharField(max_length = 90, default = "task name")
    description = models.TextField(null=True,blank=True,default = 'description')
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True)
   
    
