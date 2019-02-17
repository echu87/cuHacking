from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import classroom_creating

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request,"projects/main.html",{'first_name':request.user.first_name})
    else:
        return render(request,"projects/main.html",{'first_name':None})

def classroom(request):
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

    if request.user.is_authenticated:
        filtered = Classroom.objects.filter(teacherEmail=request.user.email)
        return render(request,"projects/classroom.html",{'first_name':request.user.first_name,'createdClasses':filtered,'createdClassesLen':len(filtered),"cform":cform})
    else:
        return render(request,"projects/classroom.html",{'first_name':None,'createdClasses':[],'createdClassesLen':0,"cform":cform})

def classroom_delete(code):
    Classroom.objects.get(code=code.delete).delete()
    

def generateClassID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))