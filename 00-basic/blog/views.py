from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Home Page of the Blog App!</h1>")

def blog(request, id):
    return HttpResponse(f"<h1>Blog ID: {id}</h1>")