from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
import random
from .forms import classroom_creating

def homepage(request):
    return render(request,"projects/main.html",{'msg':Classroom.objects.order_by('id')})
def classroom(request):
    if request.method == 'POST' and request.user.is_authenticated and not request.POST.getlist('code'):
        cform = classroom_creating(request.POST)
        if cform.is_valid():
            new_Classroom = cform.save(commit = False)
            new_Classroom.code = generateClassID()
            new_Classroom.teacherEmail = request.user.email
            new_Classroom.save()
            return redirect('/classroom')
    else:
        cform = classroom_creating()

    if request.method == 'POST' and request.user.is_authenticated and request.POST.getlist('code'):
        for classroom in Classroom.objects.order_by('code'):
            if request.POST.getlist('code')[0] == classroom.code:
                newclass = classroom
                newclass.students.add(request.user)
                newclass.save()

    if request.user.is_authenticated:
        followedClasses = []
        for classroom in Classroom.objects.order_by("students") :
            for student in classroom.students.all():
                if student.email == request.user.email and not classroom in followedClasses:
                    followedClasses.append(classroom)
        filterClasses = Classroom.objects.filter(owner = request.user.email)
        return render(request,"projects/classroom.html",{'first_name':request.user.first_name,'createdClasses':filterClasses,'createdClassesLen':len(filterClasses),'followedClasses':followedClasses,'followedClassesLen':len(followedClasses),"cform":cform})
    else:
        return render(request,"projects/classroom.html",{'first_name':None,'createdClasses':[],'createdClassesLen':0,'followedClasses':[],'followedClassesLen':0,"cform":cform})
    
def generateClassID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))

# @login_required
def join_class(request):
    if request.method == 'POST':
        for classroom in Classroom.objects.order_by('code'):
            if request.POST.getlist('code')[0] == classroom.code:
                newclass = classroom
                newclass.students.add(request.user)
                newclass.save()
                return render(request,'projects/join_class.html',{'msg': "You made it!"})                
        return render(request,'projects/join_class.html',{'msg': request.POST.getlist('code')[0]})
    else:
        return render(request,'projects/join_class.html',{'msg': ""}) 

def coloring (request, project_number):
    context = {'classroom' : Classroom.objects.get(id = project_number),'tasks': Task.objects.filter(classroom = Classroom.objects.get(id = project_number))}
    return render(request,'projects/coloring.html',context)