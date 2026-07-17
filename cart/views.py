from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart
from myapp.models import Product
from django.shortcuts import get_object_or_404

def add_to_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        print(f"product_id: {product_id}, product_quantity: {product_quantity}")
        product = get_object_or_404(Product, id=product_id)
        cart.add_to_cart(product, product_quantity)
        cart_quantity = cart.__len__()
    return JsonResponse({'qty':cart_quantity})
