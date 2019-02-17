from django.db import models
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Classroom(models.Model):
    code = models.CharField(max_length = 90, default = "class code")
    teacherEmail = models.CharField(max_length = 90, default = "teacher email")
    description = models.CharField(max_length = 90, default = "description")
    name = models.CharField(max_length = 90, default = "teacher name")
    subject = models.CharField(max_length = 90, default = "class subject")
    students = models.ManyToManyField(User)

class Task(models.Model):
    name = models.CharField(max_length = 90, default = "task name")
    description = models.TextField(null=True,blank=True,default = 'description')
    classroom = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null = True)
