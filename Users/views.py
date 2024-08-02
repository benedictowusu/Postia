from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SigninForm, SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def Signin(request):
    if request.method == 'POST':
        form = SigninForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
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