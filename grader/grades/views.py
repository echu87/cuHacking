from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
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
