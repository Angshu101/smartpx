from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Product(models.Model):
    prod_name=models.CharField(max_length=255,default="smartpx")
    disp_name=models.CharField(max_length=255,default="smartpxdisp")
    price=models.CharField(max_length=10,default="140$")
    discount_price=models.CharField(max_length=10,default="300$")
    video_URL=models.CharField(max_length=255,blank=True)
    description=RichTextField()
    created_at=models.DateTimeField(auto_now_add=True)
    best_seller=models.BooleanField(default=False)
    hot_deals=models.BooleanField(default=False)
    def __str__(self):
        return self.prod_name