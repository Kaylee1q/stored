from django.shortcuts import render
from .models import Product
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'storeProducts/index.html')

def products(request):
    return render(request, 'storeProducts/products.html')

def products_list(request):
    items = Product.objects.all()  # Get all products from DB
    return render(request, 'storeProducts/products.html', {'products': items})

def product_detail(request, pk):
    item = get_object_or_404(Product, pk=pk)
    return render(request, 'storeProducts/detail.html', {'product': item})
