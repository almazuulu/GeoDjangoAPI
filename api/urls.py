from django.urls import path, include
from .views import *

urlpatterns = [
    path('', apiOverview, name = 'api-overview'),
    path('providers/', getAllProviders, name = 'providerslist'),
    path('provider/<str:pk>', providerDetail, name = 'provider-detail'),
    path('provider-create/', providerCreate, name = 'provider-create'),
    path('provider-update/<str:pk>', providerUpdate, name = 'provider-update'),
    path('provider-delete/<str:pk>', providerDelete, name = 'provider-delete'),

    path('serviceareas/', getListServiceAreas, name='service-areas'),
    path('servicearea/<str:pk>', serviceAreaDetail, name = 'servicearea-detail'),
    path('servicearea-create/', serviceAreaCreate, name = 'servicearea-create'),
    path('servicearea-update/', serviceAreaUpdate, name = 'servicearea-update'),
    path('servicearea-delete/<str:pk>', serviceAreaDelete, name = 'servicearea-delete'),

]