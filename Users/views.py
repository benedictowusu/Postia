from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SigninForm, SignupForm
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            backend = settings.AUTHENTICATION_BACKENDS[0]
            user = authenticate(email=signupform.cleaned_data.get('email'), password=signupform.cleaned_data.get('password1'), backend=backend)
            login(request, user, backend=backend)
            return redirect('home:home')
    else:
        signupform = SignupForm()
    return render(request, 'signup.html', {'signupform': signupform})

def Signin(request):
    if request.method == 'POST':
        signinform = SigninForm(request, data=request.POST)
        if signinform.is_valid():
            email = signinform.cleaned_data.get('username')
            password = signinform.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect("home:home")
    else:
        signinform = SigninForm()
    return render(request, 'signin.html', {'signinform': signinform})

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home:home')