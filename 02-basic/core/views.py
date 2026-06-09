from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DummyForm, StudentForm

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
            request.POST
        )
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = StudentForm()
        return render(
            request,
            "form.html",
            {
                "form": form
            }
        )