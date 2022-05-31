from django.contrib.gis.db import models
import uuid
from provider.models import Provider
from djmoney.models.fields import MoneyField
from django.contrib.gis.geos import Point

from django.utils.translation import gettext_lazy as _

class ServiceArea(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    lat = models.FloatField(_("Latitude"), null=True)
    lon = models.FloatField(_("Longitude"), null=True)
    location = models.PointField(srid=4326, null=True, blank=True)
    price = MoneyField(max_digits=19, decimal_places=8, default=None)

    class Meta:
        ordering = ['service_name']

    def __str__(self):
        return self.service_name

    def save(self, *args, **kwargs):
        self.location = Point(float(self.lon), float(self.lat), srid=4326)
        super(ServiceArea, self).save(*args, **kwargs)


