from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.utils import json

from provider.models import Provider
from servicearea.models import ServiceArea

from .serializers import ProviderSerializer, ServiceareaSerializer

#Testing Provider
class TestProvider(APITestCase):

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

    def test_delete_providers(self):
        #process
        response = self.client.delete(self.url_provider_delete)

        #assert
        self.assertEquals(200, response.status_code)
        self.assertFalse(Provider.objects.filter(pk=self.id))

    def test_provider_details(self):
        #process
        response = self.client.get(self.url_provider_detail)
        self.assertEqual(200, response.status_code)

        provider_serializer_data = ProviderSerializer(instance=self.provider).data
        response_data = json.loads(response.content)

        #assert
        self.assertEqual(provider_serializer_data, response_data)


#Testing Service Area
class TestServiceArea(APITestCase):

    def setUp(self):
        self.provider_id = '682bd036-bff3-460e-88f6-7e66b5f52df6'
        self.name = 'Provider 1'
        self.email = 'provider1@gmail.com'
        self.phone = "+12125552399"
        self.language = 'en'
        self.currency = 'USD'

        self.provider = Provider.objects.create(id=self.provider_id, name=self.name, email='provider1@gmail.com',
                                                phone="+12125552399", language='en', currency='USD')


        self.servicearea_id = '171b72e2-e6fd-4f8a-a6c0-7a3475485410'
        self.provider_sa = self.provider.id
        self.service_name = 'Service 1'
        self.latidute = 40.68935514527378
        self.longitude = -74.04489740631145
        self.price = 500

        self.serviceArea = ServiceArea.objects.create(id=self.servicearea_id, provider= self.provider,
                                                      service_name = self.service_name, lat=self.latidute,
                                                      lon = self.longitude, price=self.price)

        # all urls
        self.url = reverse("service-areas")
        self.url_create_sa = reverse("servicearea-create")
        self.url_update_sa = reverse("servicearea-update", kwargs={
            "pk": self.serviceArea.pk
        })
        self.url_sa_detail = reverse(
            "servicearea-detail", kwargs={
                "pk": self.serviceArea.pk})

        self.url_sa_delete = reverse(
            "servicearea-delete", kwargs={
                "pk": self.serviceArea.pk})


    def testServiceAreaList(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

        servicearea_serializer_data = json.dumps(ServiceareaSerializer(instance=self.serviceArea).data)
        servicearea_serializer_data = [json.loads(servicearea_serializer_data)]

        # process

        self.assertEqual(servicearea_serializer_data[0]["properties"]["service_name"], "Service 1")
        self.assertEqual(servicearea_serializer_data[0]["properties"]["provider"], '682bd036-bff3-460e-88f6-7e66b5f52df6')
        self.assertEqual(servicearea_serializer_data[0]["properties"]["lat"],40.68935514527378)
        self.assertEqual(servicearea_serializer_data[0]["properties"]["lon"], -74.04489740631145)
        self.assertEqual(servicearea_serializer_data[0]["properties"]["price"], '500.00000000')

    def test_create_service_area(self):
        # definition of test data to post
        data = {
            "service_name": "Service Area 3",
            "lat": 29.979318122362827,
            "lon": 31.133611811660373,
            "price": 1000
        }

        # process
        response = self.client.post(self.url_create_sa, data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result["properties"]["service_name"], "Service Area 3")
        self.assertEqual(result["properties"]["lat"], 29.979318122362827)
        self.assertEqual(result["properties"]["lon"], 31.133611811660373)
        self.assertEqual(result["properties"]["price"], '1000.00000000')


    def test_update_service_area(self):
        #test data to update
        data = {
            "service_name": "Service Area 3"
        }

        response = self.client.patch(self.url_update_sa, data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["properties"]["service_name"], "Service Area 3")

    def test_delete_service_area(self):
        # process
        response = self.client.delete(self.url_sa_delete)

        # assert
        self.assertEquals(200, response.status_code)
        self.assertFalse(ServiceArea.objects.filter(pk=self.servicearea_id))

    def test_sa_details(self):
        # process
        response = self.client.get(self.url_sa_detail)
        self.assertEqual(200, response.status_code)

        sa_serializer_data = ServiceareaSerializer(instance=self.serviceArea).data
        response_data = json.loads(response.content)

        # assert
        self.assertEqual(sa_serializer_data, response_data)





