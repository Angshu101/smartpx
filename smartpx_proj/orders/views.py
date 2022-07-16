from http import client
from django.shortcuts import render,get_object_or_404
from mysqlx import Auth
from sklearn.metrics import auc
from .models import Order
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def orders(request):
    return render(request,'orders/orders.html')
