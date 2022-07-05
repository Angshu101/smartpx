from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'webpages/home.html')

def product(request):
    return render(request,'webpages/product.html')

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')