from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
from grades.forms import classroom_creating

from .forms import classroom_creating

# Create your views here.
def homepage(request):
    return render(request,"projects/main.html",{'msg':Classroom.objects.order_by('id')})
def classroom(request):
    if request.user.is_authenticated:
        return render(request,"projects/classroom.html",{'first_name':request.user.first_name})
    else:
        return render(request,"projects/classroom.html",{'first_name':None})

def classroom_create(request):
    if request.method == 'POST':
        cform = classroom_creating(request.POST)
        if cform.is_valid():
            new_Classroom = cform.save(commit = False)
            new_Classroom.save()
            return redirect('/classroom')
    else:
        cform = classroom_creating()
    return render(request,'projects/classroom_create.html',{"cform" : cform}) 
