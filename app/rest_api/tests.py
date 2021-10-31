import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from rest_api.serializers import *

client = APIClient()


class GetAllCitiesTest(TestCase):
    def setUp(self):
        City.objects.create(name='Москва')
        City.objects.create(name='Ростов-на-Дону')
        City.objects.create(name='Киев')

    def test_get_all_cities(self):
        response = client.get(reverse('city-list'))

        cities = City.objects.all().order_by('name')
        serializer = CitySerializer(cities, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class GetCityDetailTest(TestCase):
    def setUp(self):
        self.moscow = City.objects.create(name='Москва')

    def test_get_valid_city(self):
        response = client.get(
            reverse('city-detail', kwargs={'pk': self.moscow.pk})
        )

        city = City.objects.get(pk=self.moscow.pk)
        serializer = CitySerializer(city)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_city(self):
        response = client.get(
            reverse('city-detail', kwargs={'pk': 10})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewCityTest(TestCase):
    def setUp(self):
        self.valid_city_data = {
            'name': 'Москва',
        }
        self.invalid_city_data = {
            'name': '',
        }

    def test_create_valid_city(self):
        response = client.post(
            reverse('city-list'),
            data=json.dumps(self.valid_city_data),
            content_type='application/json'
        )

        city = City.objects.last()
        serializer = CitySerializer(city)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_create_invalid_city(self):
        response = client.post(
            reverse('city-list'),
            data=json.dumps(self.invalid_city_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateCityTest(TestCase):
    def setUp(self):
        self.moscow = City.objects.create(name='Москва')

        self.valid_update_city_data = {
            'name': 'Ростов',
        }
        self.invalid_update_city_data = {
            'name': '',
        }

    def test_update_valid_city(self):
        response = client.put(
            reverse(
                'city-detail',
                kwargs={'pk': self.moscow.pk}
            ),
            data=json.dumps(self.valid_update_city_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        city = City.objects.last()
        serializer = CitySerializer(city)

        self.assertEqual(response.data, serializer.data)

    def test_update_invalid_city(self):
        response = client.post(
            reverse('city-list'),
            data=json.dumps(self.invalid_update_city_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
