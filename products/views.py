from django.shortcuts import render

def index(request):
    return render(request, 'storeProducts/index.html')

def products(request):
    return render(request, 'storeProducts/products.html')
