from django.shortcuts import render
from .models import Product, Watch

def home(request):
    products = Product.objects.all()
    watches = Watch.objects.all()
    return render(request, 'home/home.html',{'products':products,'watches':watches})
