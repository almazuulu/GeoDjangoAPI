from rest_framework import serializers
from provider.models import Provider
from servicearea.models import ServiceArea

class ServiceareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    serviceArea = serializers.SerializerMethodField()

    class Meta:
        model = Provider
        fields = '__all__'

    def get_serviceArea(self, obj):
        serviceAreas = obj.servicearea_set.all()
        serializers = ServiceareaSerializer(serviceAreas,many=True)

        return serializers.data


