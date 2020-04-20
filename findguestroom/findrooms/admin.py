from django.contrib import admin

# Register your models here.

from .models import HouseAd, HouseOwner

admin.site.register(HouseAd)
admin.site.register(HouseOwner)
