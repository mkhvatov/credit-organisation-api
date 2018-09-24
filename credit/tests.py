import requests
from django.test import TestCase
from rest_framework.reverse import reverse


class TestPartnerAPI(TestCase):
    api_url = 'http://127.0.0.1:8000{}'.format(reverse('client-form-list'))
    valid_headers = {'Authorization': 'Token 9819e0037ace25c28390465b81a75dce28972dc6'}
    invalid_headers = {'Authorization': 'Token invalid_token'}

    def test_partner_api_for_permission(self):
        request = requests.get(self.api_url, headers=self.valid_headers)
        self.assertEqual(request.status_code, 200)
        request = requests.get(self.api_url, headers=self.invalid_headers)
        self.assertEqual(request.status_code, 403)


class TestCreditOrganizationAPI(TestCase):
    api_url = 'http://127.0.0.1:8000{}'.format(reverse('credit-proposals-list'))
    valid_headers = {'Authorization': 'Token e74e39708147646b989c08d907754cbc046f1eb6'}
    invalid_headers = {'Authorization': 'Token invalid_token'}

    def test_credit_organization_api_for_permission(self):
        request = requests.get(self.api_url, headers=self.valid_headers)
        self.assertEqual(request.status_code, 200)
        request = requests.get(self.api_url, headers=self.invalid_headers)
        self.assertEqual(request.status_code, 403)
