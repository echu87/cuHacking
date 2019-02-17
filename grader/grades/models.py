from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Classroom(models.Model):
<<<<<<< HEAD
    code = models.CharField(max_length = 90, default = "class code")
    teacherEmail = models.CharField(max_length = 90, default = "teacher email")
    description = models.CharField(max_length = 90, default = "description")
    name = models.CharField(max_length = 90, default = "teacher name")
    subject = models.CharField(max_length = 90, default = "class subject")
    students = models.ManyToManyField(User)
=======
    code = models.CharField(max_length = 90, default = "Code")
    owner = models.CharField(max_length = 90, default = "Email")
    subject = models.CharField(max_length = 90, default = "Enter Subject Here...")
    name = models.CharField(max_length = 90, default = "Enter Name Here...")
    description = models.CharField(max_length = 90, default = "Enter Description Here...")
    students = models.ManyToManyField(User)
    
# class Humans(models.Model):
#     email = models.CharField(max_length = 90, default = "email")
>>>>>>> origin/matt

class Task(models.Model):
    name = models.CharField(max_length = 90, default = "task name")
    description = models.TextField(null=True,blank=True,default = 'description')
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True)
