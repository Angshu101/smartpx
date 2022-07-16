from django.conf import settings
from django.db import models

# Create your models here.

class Order(models.Model):
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    state=models.CharField(max_length=100)
    transaction_id=models.CharField(max_length=150,default=0)
    total_amount=models.CharField(max_length=150,default=0)
    
    def __str__(self):
        return self.name