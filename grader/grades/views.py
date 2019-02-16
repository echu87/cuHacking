from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def homepage(request):
    return render(request,"projects/main.html")

def genClassID():
    return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(8))



print(genClassID())