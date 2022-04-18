from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(min_length=4, max_length=30, widget= forms.TextInput(attrs= {'placeholder':"Username"}))

    first_name = forms.CharField (min_length =2, max_length = 50, widget= forms.TextInput(attrs= {'placeholder':'Name'}))

    last_name= forms.CharField (min_length =2, max_length = 50, widget= forms.TextInput(attrs= {'placeholder':'Last name'}))

    email = forms.EmailField(min_length=6, max_length= 70, widget=forms.EmailInput(attrs= {'placeholder':'Email'}))

    password1 = forms.CharField (max_length = 70, widget=forms.PasswordInput(attrs= {'placeholder':'Password'}))

    password2 = forms.CharField (max_length =70, widget=forms.PasswordInput(attrs= {'placeholder':'Confirm password'}))

    def clean_email(self):
        email = self.cleaned_data["email"]
        exist = User.objects.filter(email__iexact=email).exists()

        if exist:
            raise forms.ValidationError("This email already exists, please try another")
        return email

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
