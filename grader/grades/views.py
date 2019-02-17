from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
<<<<<<< HEAD
from grades.forms import classroom_creating
=======
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
>>>>>>> origin/matt

from .forms import classroom_creating

# Create your views here.
def homepage(request):
    return render(request,"projects/main.html",{'msg':Classroom.objects.order_by('id')})
def classroom(request):
    if request.user.is_authenticated:
        filtered = Classroom.objects.filter(teacherEmail=request.user.email)
        print (filtered)
        return render(request,"projects/classroom.html",{'first_name':request.user.first_name,'createdClasses':filtered})
    else:
        return render(request,"projects/classroom.html",{'first_name':None,'createdClasses':[]})

def classroom_create(request):
    if request.method == 'POST' and request.user.is_authenticated:
        cform = classroom_creating(request.POST)
        if cform.is_valid():
            new_Classroom = cform.save(commit = False)
            new_Classroom.code = generateClassID()
            new_Classroom.teacherEmail = request.user.email
            new_Classroom.save()
            return redirect('/classroom')
    else:
        cform = classroom_creating()
    return render(request,'projects/classroom_create.html',{"cform" : cform}) 
<<<<<<< HEAD
=======

def generateClassID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))
>>>>>>> origin/matt
