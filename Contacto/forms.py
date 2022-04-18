from django import forms
from .models import Solicitudes

class ContactForm(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = '__all__'