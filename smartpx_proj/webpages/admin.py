from django.contrib import admin
from pkg_resources import cleanup_resources
from .models import Product
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    # def myphoto(self, object):
    #     return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    list_display = ('id','prod_name','disp_name','price','created_at','best_seller','hot_deals')
    list_display_links=('id','prod_name',)
    search_fields=('prod_name','price',)
    list_filter=('price',)
    list_editable=('best_seller','hot_deals')

admin.site.register(Product,ProductAdmin)
