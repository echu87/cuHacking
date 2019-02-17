from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task

from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ClassForm

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request,"projects/main.html",{'first_name':request.user.first_name})
    else:
        return render(request,"projects/main.html",{'first_name':None})

def classroom(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            print(form)
            form = ClassForm()
    else:
        form = ClassForm()

    if request.user.is_authenticated:
        return render(request,"projects/classroom.html",{'first_name':None,'form':form})
    else:
        return render(request,"projects/classroom.html",{'form':form})
