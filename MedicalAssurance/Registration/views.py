from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    user_name = 'zeesun and Rafa'
    return render(request,'home.html',{'name': user_name})