from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def birthdayPragati(request):
    return HttpResponse("<h1> My birthday is on 3 August </h1>")