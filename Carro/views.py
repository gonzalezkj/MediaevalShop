import re
from django.shortcuts import redirect
from .carro import Carro
from django.contrib.auth.decorators import login_required
from Shop.models import Product

# Create your views here.

@login_required
def add(request, product_id):
    carro = Carro(request)
    product = Product.objects.get(id=product_id)
    carro.add(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'Shop'))

@login_required
def remove(request, product_id):
    carro = Carro(request)
    product = Product.objects.get(id=product_id)
    carro.remove(product)
    return redirect(request.META.get('HTTP_REFERER', 'Shop'))

@login_required
def decrement(request, product_id):
    carro = Carro(request)
    product = Product.objects.get(id=product_id)
    carro.decrement(product=product)
    return redirect(request.META.get('HTTP_REFERER', 'Shop'))

@login_required
def clear(request):
    carro = Carro(request)
    carro.clear()
    return redirect(request.META.get('HTTP_REFERER', 'Shop'))