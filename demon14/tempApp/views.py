from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    m = { 'name' : 'Pratush', 'age':'25'}
    return render(request , 'tempApp/alp.html',context=m) 

def empDetails(request):
    m1 = {'name':'Pratush','age':26,'salary': 13500 }
    return render(request , 'tempApp/emp.html', m1)