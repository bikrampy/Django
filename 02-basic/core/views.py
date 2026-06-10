from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DummyForm, StudentForm
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'home.html')

def dummyform(request):
    if request.method == 'POST':
        form = DummyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return redirect('home')
    else:
        form = DummyForm()
        return render(
            request,
            "dummyform.html",
            {
                "form": form
            }
        )
    
def studentform(request):
    if request.method == "POST":
        form = StudentForm(
            request.POST, request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("Form Errors:", form.errors)
    else:
        form = StudentForm()
        return render(
            request,
            "form.html",
            {
                "form": form
            }
        )

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect("login")
    return render(request, 'signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(
                request,
                user
            )
            return redirect(
                "dashboard"
            )
    return render(
        request,
        "login.html"
    )

def logout_user(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    return render(
        request,
        "dashboard.html"
    )