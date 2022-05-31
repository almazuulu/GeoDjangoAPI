from rest_framework import serializers
from provider.models import Provider
from servicearea.models import ServiceArea
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class ServiceareaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ('service_name', 'provider', 'lat', 'lon', 'price')
        geo_field = "location"

class ProviderSerializer(serializers.ModelSerializer):
    serviceArea = serializers.SerializerMethodField()

    class Meta:
        model = Provider
        fields = '__all__'

    def get_serviceArea(self, obj):
        serviceAreas = obj.servicearea_set.all()
        serializers = ServiceareaSerializer(serviceAreas,many=True)

        return serializers.data


