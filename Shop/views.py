from django.shortcuts import render
from Shop.models import Category, Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required
def shop(request):
    return render(request, "Shop/shop.html")

@login_required
def boats(request):
    product = Product.objects.all()
    category = Category.objects.get(name="Boats")
    p = Paginator(Product.objects.filter(categories_id=1), 2)
    page = request.GET.get('page')
    productos = p.get_page(page)
    return render(request, "Shop/boats.html", {"product":product, "category":category, "productos": productos})

@login_required
def horses(request):
    product = Product.objects.all()
    category = Category.objects.get(name="Horses")
    p = Paginator(Product.objects.filter(categories_id=4), 2)
    page = request.GET.get('page')
    productos = p.get_page(page)
    return render(request, "Shop/horses.html", {"product":product, "category":category, "productos": productos})

@login_required
def carriages(request):
    product = Product.objects.all()
    category = Category.objects.get(name="Carriages")
    p = Paginator(Product.objects.filter(categories_id=2), 2)
    page = request.GET.get('page')
    productos = p.get_page(page)
    return render(request, "Shop/carriages.html", {"product":product, "category":category, "productos": productos})

@login_required
def swords(request):
    product = Product.objects.all()
    category = Category.objects.get(name="Swords")
    p = Paginator(Product.objects.filter(categories_id=6), 2)
    page = request.GET.get('page')
    productos = p.get_page(page)
    return render(request, "Shop/swords.html", {"product":product, "category":category, "productos": productos})

@login_required
def shields(request):
    product = Product.objects.all()
    category = Category.objects.get(name="Shields")
    p = Paginator(Product.objects.filter(categories_id=5), 2)
    page = request.GET.get('page')
    productos = p.get_page(page)
    return render(request, "Shop/shields.html", {"product":product, "category":category, "productos": productos})

@login_required
def helmets(request):
    product = Product.objects.all()
    category = Category.objects.get(name="Helmets")
    p = Paginator(Product.objects.filter(categories_id=3), 2)
    page = request.GET.get('page')
    productos = p.get_page(page)
    return render(request, "Shop/helmets.html", {"product":product, "category":category, "productos": productos})
