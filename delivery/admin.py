from django.contrib import admin

# Register your models here.
from .models import Deliver
class DeliveryAdmin(admin.ModelAdmin):
     deliver_method=("date"," delivery_cost"," order_status ","delivery_method","delivery_person ")
     admin.site.register(Deliver)

