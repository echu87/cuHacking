<<<<<<< HEAD

from django import forms

class ClassForm(forms.Form):
    teacher = forms.CharField(label='Teacher', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
=======
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from grades.models import Classroom
from django import forms

class classroom_creating(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ['humans']
>>>>>>> origin/youssef
