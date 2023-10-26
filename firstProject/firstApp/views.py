from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def test(request):
    return HttpResponse("<h1>Hi !! This is Prstush</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current Date and Time :</b>"+ str(dt)
    return HttpResponse(s)
