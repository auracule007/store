from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'email', 'pix', 'phone_no','age','address']
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'pix': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Load Image'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Address'}),
        }

class ShopcartForm(forms.ModelForm):
    class Meta:
        model = Shopcart
        fields = ['quantity']

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']