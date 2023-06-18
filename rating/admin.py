from django.contrib import admin

# Register your models here.
from .models import Rates
class RegistrationAdmin(admin.ModelAdmin):
    details_display=("review_message","sender"," value","date","product")
    admin.site.register(Rates)