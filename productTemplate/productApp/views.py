from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict = {
        'heading':'Electronics',
        'product1' : 'Mac',
        'product2' : 'iPhone',
        'product3' : 'Samsung'
    }
    return render(request, 'productApp/products.html', product_dict)

def toys(request):
    product_toy = {
        'heading':'Toy',
        'product1' : 'Apple',
        'product2' : 'Nintendo',
        'product3' : 'Microsoft'
    }
    return render(request, 'productApp/products.html', product_toy)

def shoes(request):
    product_shoes = {
        'heading':'Shoes',
        'product1' : 'Nike',
        'product2' : 'Adidas',
        'product3' : 'Puma'
    }
    return render(request,'productApp/products.html', product_shoes)

def index(request):
    return render(request, 'productApp/index.html')