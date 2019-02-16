from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

level_percentages = {"4++":100, "4+":97, "4/4+":95, "4":92, "4-/4":87, "4-":83, "3+/4-":80, "3+":78, "3/3+":76, "3":75, "3-/3":73, "3-":71, "2+/3-":70, "2+":68, "2/2+":66, "2":64, "2-/2":62, "1+/2-":60, "1+":59, "1/1+":57, "1":55, "1-/1":53, "1-":51}

def homepage(request):
    return render(request,"projects/main.html")

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


print(suggest_mark(["3+/4-","2+/3-", "3", "1"]))

