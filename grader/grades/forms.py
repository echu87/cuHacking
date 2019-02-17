from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from grades.models import Classroom, Task,Marks
from django import forms

class classroom_creating(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ['code','owner','students']


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['classroom','keyword','']

class Mark_form(forms.ModelForm):
    class Meta:
        model = Marks
        exclude = ['task','student']
