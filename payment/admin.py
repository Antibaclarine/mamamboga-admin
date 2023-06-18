from django.contrib import admin

# Register your models here.
from .models import Pay
class PayAdmin(admin.ModelAdmin):
    details_display=("amount","order","status ","date","method_payment")
    admin.site.register(Pay)