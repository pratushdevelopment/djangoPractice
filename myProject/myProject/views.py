from django.shortcuts import render

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})

def home(request):
    return render(request,'home.html',{})

def services(request):
    return render(request,'services.html',{})

def navbar(request):
    return render(request,'navbar.html',{})