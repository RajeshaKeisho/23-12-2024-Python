from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<html><body><h1>About Us</h1><p>This is about Page</p>'
    '</body></html>')

def sample_view(request):
    if 'error' in request.GET:
        raise ValueError("It is a simple Value Error")
    return HttpResponse("no error occurred!")