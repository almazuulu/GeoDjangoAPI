from django.urls import path, include
from .views import *

urlpatterns = [
    path('', apiOverview, name = 'api-overview')
]