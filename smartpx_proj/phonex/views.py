from django.shortcuts import render
from webpages.models import Product
# Create your views here.
def phonex(request):
    pass
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
