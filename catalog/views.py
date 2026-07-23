from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    products = Product.objects.filter(active=True)
    return render(request, 'catalog/index.html', {'products': products})

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug, active=True)
    return render(request, 'catalog/detail.html', {'product': product})



