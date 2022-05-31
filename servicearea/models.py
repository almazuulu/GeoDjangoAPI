from django.contrib.gis.db import models
import uuid

from rest_framework.utils import json

from provider.models import Provider
from djmoney.models.fields import MoneyField
from django.contrib.gis.geos import Point, Polygon

from django.utils.translation import gettext_lazy as _

class ServiceArea(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    # lat = models.FloatField(_("Latitude"), null=True)
    # lon = models.FloatField(_("Longitude"), null=True)
    lat1 = models.FloatField(_("Latitude 1"), null=True, blank=True)
    lon1 = models.FloatField(_("Longitude 1"), null=True, blank=True)
    lat2 = models.FloatField(_("Latitude 2"), null=True, blank=True)
    lon2 = models.FloatField(_("Longitude 2"), null=True,blank=True)
    lat3 = models.FloatField(_("Latitude 3"), null=True, blank=True)
    lon3 = models.FloatField(_("Longitude 3"), null=True, blank=True)
    lat4 = models.FloatField(_("Latitude 4"), null=True, blank=True)
    lon4 = models.FloatField(_("Longitude 4"), null=True, blank=True)
    location = models.PolygonField(srid=4326, null=True, blank=True)
    price = MoneyField(max_digits=19, decimal_places=8, default=None)

    class Meta:
        ordering = ['service_name']

    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        coordinate_pair1 = (self.lat1, self.lon1)
        coordinate_pair2 = (self.lat2, self.lon2)
        coordinate_pair3 = (self.lat3, self.lon3)
        coordinate_pair4 = (self.lat4, self.lon4)

        coord_list = (coordinate_pair1, coordinate_pair2, coordinate_pair3, coordinate_pair4, coordinate_pair1)
        self.location = Polygon(coord_list)

        super(ServiceArea, self).save(*args, **kwargs)


