from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=250)
    last_name = forms.CharField(max_length=250)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "password1", "password2")
        

class SigninForm(AuthenticationForm):
    username = forms.EmailField(label='Email', max_length=254)