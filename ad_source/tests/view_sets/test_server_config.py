from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestSubscribeView(APITestCase):
    def setUp(self):
        self.url = reverse('server_config-list')

    def test_get_server_config(self):
        expected = {'public_key': '0xDd2179e8D8755f810CdAe4a474F7c53F371FbB6A'}
        response = self.client.get(self.url)
        data = response.json()
        self.assertEqual(data, expected)

    def test_create_server_config(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_server_config(self):
        response = self.client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
