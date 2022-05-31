from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from provider.models import Provider
from servicearea.models import ServiceArea
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'

class ServiceareaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer(read_only=True)
    provider_id = PrimaryKeyRelatedField(
        queryset=Provider.objects.all(),
        required=True, write_only=True, source='provider')

    class Meta:
        model = ServiceArea
        fields = ('id', 'service_name', 'provider', 'provider_id', 'lat', 'lon', 'price')
        geo_field = "location"


