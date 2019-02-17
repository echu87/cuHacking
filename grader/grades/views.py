from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Classroom, Task, Marks
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import classroom_creating,Mark_form,Task_form

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return render(request,"projects/main.html",{'first_name':request.user.first_name})
    else:
        return render(request,"projects/main.html",{'first_name':None})

def classroom(request):
    if request.method == 'POST' and request.user.is_authenticated and not request.POST.getlist('code'):
        cform = classroom_creating(request.POST)
        if cform.is_valid():
            new_Classroom = cform.save(commit = False)
            new_Classroom.code = generateClassID()
            new_Classroom.owner = request.user.email
            new_Classroom.save()
            return redirect('/classroom')
    else:
        cform = classroom_creating()

    if request.method == 'POST' and request.user.is_authenticated and request.POST.getlist('code'):
        for classroom in Classroom.objects.order_by('code'):
            if request.POST.getlist('code')[0] == classroom.code and request.user.email != classroom.owner:
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

def classroom_detail(request, project_number):
    editing = False
    if Classroom.objects.filter(id = project_number).get(owner = request.user.email):
        editing = True
    context = {'classroom' : Classroom.objects.get(id = project_number),'tasks': Task.objects.filter(classroom = Classroom.objects.get(id = project_number)), 'editing':editing}
    return render(request,'projects/classroom_detail.html', context) 

def delete_class(request,class_id):
    Classroom.objects.get(id = class_id).delete()
    return redirect('/classroom')


def enroll_class(request,class_id):
    Classroom.objects.get(id = class_id).students.remove(request.user)
    return redirect('/classroom')


# @login_required
# def join_class(request):
#     if request.method == 'POST':
#         for classroom in Classroom.objects.order_by('code'):
#             if request.POST.getlist('code')[0] == classroom.code:
#                 newclass = classroom
#                 newclass.students.add(request.user)
#                 newclass.save()
#                 return render(request,'projects/join_class.html',{'msg': "You made it!"})                
#         return render(request,'projects/join_class.html',{'msg': request.POST.getlist('code')[0]})
#     else:
#         return render(request,'projects/join_class.html',{'msg': ""}) 
def generateClassID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))


# def mark(request,class_id,task_id):
#     context = {'task': Task.objects.get(id = task_id), 'students': Classroom.objects.get(id = class_id).students.all()}
#     if request.method == 'POST':
#         form = Mark_form(request.POST)
#         return render(request,'projects/mark.html', context)
#     else:
#         return render(request,'projects/mark.html', context)

def create_task(request,class_id):
    if request.method == 'POST':
        tsform = Task_form(request.POST)
        if tsform.is_valid():
            new_Classroom = tsform.save(commit = False)
            new_Classroom.classroom = Classroom.objects.get(id = class_id)
            new_Classroom.save()
            return redirect('/classroom/'+str(class_id))
    else:
        tsform = classroom_creating()
    return render(request,'projects/ctask.html', {'form':tsform})

