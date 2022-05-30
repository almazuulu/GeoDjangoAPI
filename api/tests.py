from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json

from provider.models import Provider
from servicearea.models import ServiceArea

from .serializers import ProviderSerializer

class TestProvider(APITestCase):
    url_get_providers = "/api/providers/"

    def setUp(self):
        self.id = '682bd036-bff3-460e-88f6-7e66b5f52df6'
        self.name = 'Provider 1'
        self.email = 'provider1@gmail.com'
        self.phone = "+12125552399"
        self.language = 'en'
        self.currency = 'USD'

        self.provider = Provider.objects.create(name = self.name, email = 'provider1@gmail.com',
                            phone= "+12125552399", language='en', currency='USD')

        self.url = reverse("providerslist")
        self.provider_url = reverse(
            "provider-detail", kwargs={
                "pk": self.provider.pk})


    def test_providers(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        provider_serializer_data = json.dumps(ProviderSerializer(instance=self.provider).data)
        provider_serializer_data = [json.loads(provider_serializer_data)]

        response_data = json.loads(response.content)

        self.assertEqual(provider_serializer_data,response_data)
        self.assertEqual(provider_serializer_data[0]["name"], "Provider 1")
        self.assertEqual(provider_serializer_data[0]["email"], 'provider1@gmail.com')
        self.assertEqual(provider_serializer_data[0]["phone"], "+12125552399")
        self.assertEqual(provider_serializer_data[0]["language"], "en")
        self.assertEqual(provider_serializer_data[0]["currency"], "USD")




