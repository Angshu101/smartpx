from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    

    list_display = ('id','customer_name','email','phone','enquiry','created_at',)
    list_display_links=('id','customer_name',)
    search_fields=('customer_name','email','phone',)
    list_filter=('customer_name','email','phone',)

admin.site.register(Contact,ContactAdmin)
