from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, APIClient, \
    force_authenticate

from pollsapi import views
from pollsapi.tests.user_setup import setup_user


class TestPollDetail(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = setup_user()
        self.view = views.PollList.as_view()
        self.uri = '/polls/pk/'

    def test_unauthenticated_uri(self):
        """
        If not authorized access not allowed
        """
        request = self.factory.get(self.uri)
        response = self.view(request, pk='2')
        self.assertEqual(response.status_code, 401,
                         'Expected Response Code 401, received {0} instead.'
                         .format(response.status_code))

    def test_authenticated_uri(self):
        """
        GET
        """
        request = self.factory.get(self.uri)
        force_authenticate(request, self.user)
        response = self.view(request, pk='2')
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
