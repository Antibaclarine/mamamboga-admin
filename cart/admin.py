from django.contrib import admin

# Register your models here.
from.models import Add
class AddAdmin(admin.ModelAdmin):
    add_items=("price","quantity","shippingcost","paymentoptions")
    admin.site.register(Add)