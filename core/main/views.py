from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def product(request):
    return HttpResponse ("Product Lists")

def product_details(request, id):
    return HttpResponse (f"Product ID: {id}")
