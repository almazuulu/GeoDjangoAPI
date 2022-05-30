from django.contrib import admin
from django.contrib.gis import admin
from .models import ServiceArea

class ServiceAreaAdmin(admin.GISModelAdmin):
    default_lon = -93
    default_lat = 27
    default_zoom = 4

admin.site.register(ServiceArea, ServiceAreaAdmin)
