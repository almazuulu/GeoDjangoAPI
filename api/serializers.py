from rest_framework import serializers
from provider.models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    model = Provider
    fields = ('name','email','phone_number','language', 'currency')


