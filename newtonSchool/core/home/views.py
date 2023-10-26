from django.shortcuts import HttpResponse
from django.shortcuts import render
# Create your views here.
def home(request):
    peoples = [
        {'name': 'Pratush','age':24 },
        {'name': 'Sunny', 'age':45 },
        {'name': 'Farhan' , 'age':16 },
        {'name': 'Rahul' , 'age':13 },
        {'name': 'Debashish' , 'age': 43 },
    ]
    return render(request , 'index.html' , context = {'peoples': peoples})

def demo(request):
    context = { 'variable_name': 'Hello World',
               'variable_value': 67,
               'numbers': [1, 2,3,4,5,6,7,8,9,10] , 
               }
    return render(request , 'demo.html', context )
