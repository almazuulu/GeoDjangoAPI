from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.gis.geos import Point
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProviderSerializer, ServiceareaSerializer
from provider.models import Provider
from servicearea.models import ServiceArea
from rest_framework import generics

@api_view(['GET'])
def apiOverview(request):
    apiUrls = {
        'All providers': '/providers/',
        'Detail view': '/provider/<str:pk>/',
        'Create Provider': '/provider-create/',
        'Update Provider': '/provider-update/<str:pk>/',
        'Delete Provider':'/provider-delete/<str:pk>/',

        'All service areas': '/serviceareas/',
        'Service area Detail view': '/serviceareas/<str:pk>/',
        'Create Service area': '/servicearea-create/',
        'Update Service area': '/servicearea-update/<str:pk>/',
        'Delete Service area': '/servicearea-delete/<str:pk>/',
    }

    return Response(apiUrls)

#api to list of all providers
class ProvidersListApi(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

#api to see the detail of provider area
class ProviderDetailApi(generics.RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

#api to create provider
class ProviderCreateApi(generics.CreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

#api to update provider
class ProviderUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

#api to delete provider
class ProviderDeleteApi(generics.DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(f'Item {instance.name} was successfully deleted!')

#api to list of all service-areas
class ServiceAreasListApi(generics.ListAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceareaSerializer

#api to see the detail of service area
class ServiceDetailApi(generics.RetrieveAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceareaSerializer

#api to update service area
class ServiceAreaCreateApi(generics.CreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceareaSerializer

#api to update service area
class ServiceAreaUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceareaSerializer

#api to delete service area
class ServiceAreaDeleteApi(generics.DestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceareaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(f'Item {instance.service_name} was successfully deleted!')