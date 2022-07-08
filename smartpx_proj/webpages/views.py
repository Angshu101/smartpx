from django.shortcuts import render
from .models import Product
# Create your views here.
def home(request):
    return render(request,'webpages/home.html')

def product(request):
    product=Product.objects.all()
    data={
        
        'product':product
    }
    return render(request,'webpages/product.html',data)

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')