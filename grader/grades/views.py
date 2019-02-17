from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
from grades.forms import classroom_creating

<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
=======
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import classroom_creating

>>>>>>> origin/matt
# Create your views here.
def homepage(request):
    return render(request,"projects/main.html",{'msg':Classroom.objects.order_by('id')})

<<<<<<< HEAD
=======
def classroom(request):
    if request.user.is_authenticated:
        return render(request,"projects/classroom.html",{'first_name':request.user.first_name})
    else:
        return render(request,"projects/classroom.html",{'first_name':None})

>>>>>>> origin/matt
def classroom_create(request):
    if request.method == 'POST':
        cform = classroom_creating(request.POST)
        if cform.is_valid():
            new_Classroom = cform.save(commit = False)
            new_Classroom.save()
<<<<<<< HEAD
            return redirect('/main')
    else:
        cform = classroom_creating()
    return render(request,'projects/classroom_form.html',{"cform" : cform})
=======
            return redirect('/classroom')
    else:
        cform = classroom_creating()
    return render(request,'projects/classroom_create.html',{"cform" : cform}) 
>>>>>>> origin/matt
