from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
<<<<<<< HEAD
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
=======
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
>>>>>>> origin/matt
