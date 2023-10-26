from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def birthdayUrmila(request):
    return HttpResponse("<h1>My Birthday is 8 August </h1>")