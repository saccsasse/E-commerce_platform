from django.shortcuts import render
from django.http import JsonResponse

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
    return JsonResponse({'status': 'success'})
