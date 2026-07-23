from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .cart import Cart
from myapp.models import Product
from django.shortcuts import get_object_or_404

@require_POST
def add_to_cart(request):
    cart = Cart(request)
    product_id = int( request.POST.get('product_id'))
    product_quantity = int(request.POST.get('product_quantity'))
    product = get_object_or_404(Product, id=product_id)
    cart.add(product, product_quantity)
    cart_quantity = len(cart)
    return JsonResponse({'qty':cart_quantity})


def cart_overview(request):
    cart = Cart(request)
    return render(request, 'cart/cart-overview.html', {'cart': cart})

@require_POST
def cart_delete(request):
    cart = Cart(request)
    product_id = int(request.POST.get('product_id'))
    cart.delete(product_id=product_id)
    cart_quantity = len(cart)
    cart_total = cart.get_total_price()
    return JsonResponse({'qty':cart_quantity, 'total': str(cart_total)})

@require_POST
def cart_update(request):
    cart = Cart(request)
    product_id = int(request.POST.get('product_id'))
    product_quantity = int(request.POST.get('product_quantity'))
    cart.update(product_id=product_id, product_quantity=product_quantity)
    return JsonResponse({'qty':len(cart)})
