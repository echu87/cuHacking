
from django import forms

class ClassForm(forms.Form):
    teacher = forms.CharField(label='Teacher', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)