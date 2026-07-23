from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart
from myapp.models import Product
from django.shortcuts import get_object_or_404

def add_to_cart(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_quantity = int(request.POST.get('product_quantity'))
        print(f"product_id: {product_id}, product_quantity: {product_quantity}")
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, product_quantity)
        cart_quantity = cart.__len__()
    return JsonResponse({'qty':cart_quantity})


def cart_overview(request):
    cart = Cart(request)
    return render(request, 'cart/cart-overview.html', {'cart': cart})

def cart_delete(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart.delete(product_id=product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        return JsonResponse({'qty':cart_quantity, 'total':cart_total})


def cart_update(request):
    cart = Cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_quantity = int(request.POST.get('product_quantity'))
        cart.update(product_id=product_id, product_quantity=product_quantity)
        return JsonResponse({'qty':cart.__len__()})
