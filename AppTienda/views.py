from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from Shop.models import Product
from AppTienda.forms import ProductoForm, ModificarForm
from django.contrib import messages

# Create your views here.

@login_required
def home(request):
    return render(request, "AppTienda/home.html")

@login_required
def agregar_producto(request):

    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "The product has been add correctly")
        else:
            data["form"] = formulario
            
    return render(request, 'AppTienda/agregar.html', data)

@login_required
def modificar_producto(request, id):

    producto = get_object_or_404(Product, id=id)

    data = {
        'form': ModificarForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ModificarForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "The product has been modify correctly")
        else:
            data["form"] = formulario
        
    return render(request, 'AppTienda/modificar.html', data)