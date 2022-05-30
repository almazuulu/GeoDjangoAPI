from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProviderSerializer
from provider.models import Provider

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


@api_view(['GET'])
def getAllProviders(request):
    providers = Provider.objects.all()
    serializer = ProviderSerializer(providers, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def providerDetail(request, pk):
    provider = Provider.objects.get(pk = pk)
    serializer = ProviderSerializer(provider, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def providerCreate(request):
    serializer = ProviderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def providerUpdate(request, pk):
    provider = Provider.objects.get(pk = pk)
    serializer = ProviderSerializer(instance=provider, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def providerDelete(request, pk):
    provider = Provider.objects.get(pk = pk)
    provider.delete()

    return Response(f'Item {provider.name} was successfully deleted!')


