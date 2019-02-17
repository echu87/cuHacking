from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length = 90, default = "class name")
    subject = models.CharField(max_length = 90, default = "class")
    users = models.CharField(max_length = 90, default= "Johny Appleseed")
    owner = models.CharField(max_length = 90, default = "owner")

class Task(models.Model):
    name = models.CharField(max_length = 90, default = "task name")
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True)
    description = models.TextField(null=True,blank=True,default = 'description')
    due_date = models.DateField()

# class ClassMembers(models.Model):
#     classroom = models.ForeignKey(Classroom, on_delete = models.SET_NULL, null = True)
    
