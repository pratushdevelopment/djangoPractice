from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pratush(request):
    return HttpResponse("Hi!!!!!!!!!!!")

def mishra(request):
    return render(request,'seventeenApp/index.html',{})

def empMis(request):
    m1 = { 'name' : 'Pratush Mishra', 'age':'28','roll':'24'}
    return render(request,'seventeenApp/index.html',context=m1)