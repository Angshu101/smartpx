from django.contrib import admin
from pkg_resources import cleanup_resources
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','prod_name','disp_name','price','created_at')
    list_display_links=('id','prod_name',)
    search_fields=('prod_name','price',)
    list_filter=('price',)

admin.site.register(Product,ProductAdmin)
