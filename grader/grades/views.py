from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
import random
from .forms import create_classroom_form
from .models import Classroom
from django.shortcuts import redirect
# Create your views here.

level_percentages = {"4++":100, "4+":97, "4/4+":95, "4":92, "4-/4":87, "4-":83, "3+/4-":80, "3+":78, "3/3+":76, "3":75, "3-/3":73, "3-":71, "2+/3-":70, "2+":68, "2/2+":66, "2":64, "2-/2":62, "1+/2-":60, "1+":59, "1/1+":57, "1":55, "1-/1":53, "1-":51}

def genClassID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))

def suggest_mark(marks):
    converted_marks = []
    for i in marks:
        converted_marks.append(int(level_to_percentage(i)))
    
    sum = 0
    for i in range(len(converted_marks)):
        sum+= (converted_marks[i]) * (1+(i/50))
    
    avg = int(sum/len(converted_marks))
    return " Suggested Average:" + str(avg) + "+- 2%"
    

def level_to_percentage(level):
    return level_percentages[level]


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
=======
from django.contrib.auth.models import User
from .models import Human, Classroom, Task
from grades.forms import classroom_creating

from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def homepage(request):
    return render(request,"projects/main.html",{'msg':Classroom.objects.order_by('id')})

def classroom_create(request):
    if request.method == 'POST':
        cform = classroom_creating(request.POST)
        if cform.is_valid():
            new_Classroom = cform.save(commit = False)
            new_Classroom.save()
            return redirect('/main')
    else:
        cform = classroom_creating()
    return render(request,'projects/classroom_form.html',{"cform" : cform})
>>>>>>> origin/youssef
