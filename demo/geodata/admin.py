from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import GeoData

admin.site.register(GeoData)