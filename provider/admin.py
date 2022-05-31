from django.contrib import admin
from django.contrib.gis import admin
from .models import Provider

admin.site.register(Provider,admin.GISModelAdmin)

