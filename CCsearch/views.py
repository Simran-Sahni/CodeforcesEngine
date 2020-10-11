from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'base.html',{'name':'Simran'})

def entered(request):
    res=(request.POST["query"])
    return render(request,'result.html',{'result':res})