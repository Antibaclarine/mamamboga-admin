from django.contrib import admin

# Register your models here.
from .models import Customer
class CustomerAdmin(admin.ModelAdmin):
    add_items=("price","quantity","shippingcost","paymentoptions")
    admin.site.register(Customer)
