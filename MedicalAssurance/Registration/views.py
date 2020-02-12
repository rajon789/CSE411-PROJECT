from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    user_name = 'zeesun and Rafa'
    return render(request,'home.html',{'name': user_name})

def add(request):
    val_1 = request.POST['number1']
    val_2 = request.POST['number2']
    try:
        res = int(val_1) + int(val_2)
    except:
        return render(request,'result.html',{'result':'Not valid'})
    return render(request,'result.html',{'result':res})