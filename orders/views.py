from django.db import transaction
from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address, Order, OrderItem
from cart.cart import Cart
from django.http import JsonResponse


def add_address(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('index')
    form = AddressForm(instance=address)
    return render(request, 'orders/add_address.html', {'form': form})


def checkout(request):
    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user=request.user)
            return render(request, 'orders/checkout.html', {'address': address})
        except Address.DoesNotExist:
            return render(request, 'orders/checkout.html')
    else:
        return render(request, 'orders/checkout.html')


def place_order(request):
    order_success = False
    if request.method == "POST":
        cart = Cart(request)
        total_amount = cart.get_total_price()
        if request.user.is_authenticated:
            with transaction.atomic():
                order = Order.objects.create(user=request.user, total_amount=total_amount)
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity']
                )
            order_success = True
        else:
            with transaction.atomic():
                order = Order.objects.create(total_amount=total_amount)
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity']
                )
            order_success = True
    return JsonResponse({'success': order_success})

def order_success(request):
    return render(request, 'orders/order-success.html')

def order_failed(request):
    return render(request, 'orders/order-failed.html')