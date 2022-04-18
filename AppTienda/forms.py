from django import forms
from Shop.models import Product

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ModificarForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'