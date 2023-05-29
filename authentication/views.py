from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

# Create your views here.
def home(request):
    return render(request, "authetication/index.html")

def signup(request):
    if request.method == "GET":
        form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
    return render(request, "authetication/signup.html", {'form': form})

def signin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "authetication/signin.html", {'form':form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')
        messages.error(request, f'Invalid username or password')
        return render(request, "authetication/signin.html", {'form': form})

def signout(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('signin')