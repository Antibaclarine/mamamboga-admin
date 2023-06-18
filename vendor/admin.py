from django.contrib import admin

# Register your models here.
from .models import Registration
class RegistrationAdmin(admin.ModelAdmin):
    details_display=("name","","location","contact ","password ")
    admin.site.register(Registration)