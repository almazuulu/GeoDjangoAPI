from django.urls import path, include
from .views import *

urlpatterns = [
    path('', apiOverview, name = 'api-overview'),
    path('providers/', getAllProviders, name = 'providerslist'),
    path('provider/<str:pk>', providerDetail, name = 'provider-detail'),
    path('provider-create/', providerCreate, name = 'provider-create'),
    path('provider-update/<str:pk>', providerUpdate, name = 'provider-update'),
    path('provider-delete/<str:pk>', providerDelete, name = 'provider-delete'),
]