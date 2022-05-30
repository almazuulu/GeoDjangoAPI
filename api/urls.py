from django.urls import path, include
from .views import *

urlpatterns = [
    path('', apiOverview, name = 'api-overview'),

    #api route for providers
    path('providers/', ProvidersListApi.as_view(), name = 'providerslist'),
    path('provider/<str:pk>', ProviderDetailApi.as_view(), name = 'provider-detail'),
    path('provider-create/', ProviderCreateApi.as_view(), name = 'provider-create'),
    path('provider-update/<str:pk>', ProviderUpdateApi.as_view(), name = 'provider-update'),
    path('provider-delete/<str:pk>', ProviderDeleteApi.as_view(), name = 'provider-delete'),

    #api route for service areas
    path('serviceareas/', ServiceAreasListApi.as_view(), name='service-areas'),
    path('servicearea/<str:pk>', ServiceDetailApi.as_view(), name = 'servicearea-detail'),
    path('servicearea-create/', ServiceAreaCreateApi.as_view(), name = 'servicearea-create'),
    path('servicearea-update/<str:pk>', ServiceAreaUpdateApi.as_view(), name = 'servicearea-update'),
    path('servicearea-delete/<str:pk>', ServiceAreaDeleteApi.as_view(), name = 'servicearea-delete'),
]