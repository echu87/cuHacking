from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from grades.models import Classroom
from django import forms

class classroom_create(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ['owner', 'users']
class classroom_join(forms.ModelForm):
    class Meta:
        model = Classroom
        exclude = ['owner']

class classroom_editing(forms.ModelForm):
    class Meta:
        print("hello")
