from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
def home(request):
    print(request)
    return render(request, "home.html", {
        "heading": "Welcome to Home Page"
    })

def apiHome(request):
    return JsonResponse({
        "heading": "Welcome to Home Page"
    })

def about(request):
    return HttpResponse("<h1>Welcome to the About Page!</h1><a href='/'>Go to Home Page</a>")

def apiAbout(request):
    return JsonResponse({
        "heading": "Welcome to About Page"
    })

def profile(request):
    return redirect('home')

def portfolio(request):
    return redirect('https://www.beingbifrons.shop/')