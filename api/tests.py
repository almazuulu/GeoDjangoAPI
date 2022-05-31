from django.test import TestCase
from rest_framework import status
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

        self.provider = Provider.objects.create(id = self.id, name = self.name, email = 'provider1@gmail.com',
                            phone= "+12125552399", language='en', currency='USD')

        #all urls
        self.url = reverse("providerslist")
        self.url_create = reverse("provider-create")
        self.url_update = reverse("provider-update", kwargs={
            "pk": self.provider.pk
        })
        self.url_provider_detail = reverse(
            "provider-detail", kwargs={
                "pk": self.provider.pk})

        self.url_provider_delete = reverse(
            "provider-delete", kwargs={
                "pk": self.provider.pk})


    def test_providers(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        provider_serializer_data = json.dumps(ProviderSerializer(instance=self.provider).data)
        provider_serializer_data = [json.loads(provider_serializer_data)]

        #process
        response_data = json.loads(response.content)

        #assert
        self.assertEqual(provider_serializer_data,response_data)
        self.assertEqual(provider_serializer_data[0]["id"], "682bd036-bff3-460e-88f6-7e66b5f52df6")
        self.assertEqual(provider_serializer_data[0]["name"], "Provider 1")
        self.assertEqual(provider_serializer_data[0]["email"], 'provider1@gmail.com')
        self.assertEqual(provider_serializer_data[0]["phone"], "+12125552399")
        self.assertEqual(provider_serializer_data[0]["language"], "en")
        self.assertEqual(provider_serializer_data[0]["currency"], "USD")

    def test_create_provider(self):
        #definition of test data to post
        data = {
            "name": "Main Provider",
            "email": "mainprovider@gmail.com"
        }

        #process
        response = self.client.post(self.url_create, data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["name"], "Main Provider")

    def test_update_manufacturer(self):
        #test data to update
        data = {
            "name": "Provider 2"
        }

        response = self.client.patch(self.url_update, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], "Provider 2")

    def test_provider_details(self):
        #process
        response = self.client.get(self.url_provider_detail)
        self.assertEqual(200, response.status_code)

        provider_serializer_data = ProviderSerializer(instance=self.provider).data
        response_data = json.loads(response.content)

        #assert
        self.assertEqual(provider_serializer_data, response_data)

    def test_delete_providers(self):
        #process
        response = self.client.delete(self.url_provider_delete)

        #assert
        self.assertEquals(200, response.status_code)
        self.assertFalse(Provider.objects.filter(pk=self.id))

