from django.shortcuts import render

def about(request):
    return render(request,'about.html',{})

def navbar(request):
    return render(request,'navbar.html',{})