from django.db import models
import uuid
from provider.models import Provider

class ServiceArea(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=True, null=True)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    geojson_info = models.CharField(max_length=500, null=True, default=True)

    class Meta:
        ordering = ['service_name']


    def __str__(self):
        return self.service_name
