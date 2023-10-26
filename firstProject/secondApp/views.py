from django.shortcuts import render
from django.http import HttpResponse
import datetime

def test2(request):
    dt = datetime.datetime.now()
    message = "My Life , My Time "+ str(dt)
    return HttpResponse(message)