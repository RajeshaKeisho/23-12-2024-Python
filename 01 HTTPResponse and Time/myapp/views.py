from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

# def display(request):
#     s = "<h1>Hello, Welcome to Django Classes!</h1>"
#     return HttpResponse(s)
def morning_message(request):
    time = datetime.datetime.now()
    fomratted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Morning! now the time is" + fomratted_time + "</h1>")

def afternoon_message(request):
    time = datetime.datetime.now()
    fomratted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Afternoon! now the time is" + fomratted_time + "</h1>")

def evening_message(request):
    time = datetime.datetime.now()
    fomratted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Evening! now the time is" + fomratted_time + "</h1>")