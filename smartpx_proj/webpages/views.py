from django.shortcuts import render,get_object_or_404
from .models import Product
# Create your views here.
def home(request):
    return render(request,'webpages/home.html')

def product(request):
    product=Product.objects.all()
    best_seller=Product.objects.order_by('created_at').filter(best_seller=True)
    hot_deals=Product.objects.order_by('created_at').filter(hot_deals=True)
    data={
        
        'product':product,
        'best_seller':best_seller,
        'hot_deals':hot_deals
    }
    return render(request,'webpages/product.html',data)

def about(request):
    return render(request,'webpages/about.html')

def contact(request):
    return render(request,'webpages/contact.html')

def phone_details(request,id):
     phone_det= get_object_or_404(Product,pk=id)
     data={
         'phone_det':phone_det
     }
     return render(request,'webpages/phone_details.html',data)