from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Classroom(models.Model):
    code = models.CharField(max_length = 90, default = "Code")
    teacherEmail = models.CharField(max_length = 90, default = "Email")
    subject = models.CharField(max_length = 90, default = "Enter Subject Here...")
    name = models.CharField(max_length = 90, default = "Enter Name Here...")
    description = models.CharField(max_length = 90, default = "Enter Description Here...")
    
# class Humans(models.Model):
#     email = models.CharField(max_length = 90, default = "email")

class Task(models.Model):
    name = models.CharField(max_length = 90, default = "task name")
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True)