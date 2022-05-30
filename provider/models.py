from django.db import models
from django.contrib.gis.db import models
from djmoney.models.fields import CurrencyField
from phonenumber_field.modelfields import PhoneNumberField
import uuid
from mozio.utils import LanguageField

class Provider(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = PhoneNumberField(blank=True)
    language = LanguageField(default='en')
    currency = CurrencyField(default='USD')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


