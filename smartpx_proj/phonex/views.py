from django.shortcuts import render,redirect
from webpages.models import Product
from .models import Contact
# Create your views here.
def search(request):
    searc_ph=Product.objects.all()
    
    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            searc_ph=searc_ph.filter(prod_name__icontains=keyword)
    data={
        'searc_ph':searc_ph,
    }
    return render(request,'phonex/search.html',data)


def contct(request):
    if request.method =='POST':
        customer_name=request.POST['customer_name']
        email=request.POST['email']
        phone=request.POST['phone']
        enquiry=request.POST['enquiry']
        
        
        contact_phonex=Contact(customer_name=customer_name,email=email,phone=phone,enquiry=enquiry)
        contact_phonex.save()
        
    return redirect('home')