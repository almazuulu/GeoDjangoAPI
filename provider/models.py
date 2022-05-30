from django.db import models
import uuid

class Provider(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False),
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)
    language = models.CharField(max_length=100, null = True, blank=True)
    currency = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



