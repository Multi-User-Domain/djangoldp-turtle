import uuid
import json

from djangoldp.serializers import LDListMixin, LDPSerializer
from rest_framework.test import APITestCase, APIClient

from djangoldp_turtle.tests.models import TurtleCircle
from djangoldp_turtle.tests.utils import get_random_user


class ViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        LDListMixin.to_representation_cache.reset()
        LDPSerializer.to_representation_cache.reset()

    def setUpLoggedInUser(self):
        self.user = get_random_user()
        self.client.force_authenticate(user=self.user)

    def _get_random_circle(self):
        return TurtleCircle.objects.create(name='Test')

    def test_circles_list(self):
        self.setUpLoggedInUser()
        circle = self._get_random_circle()

        response = self.client.get('/turtlecircles/', HTTP_ACCEPT='text/turtle', format='ttl')
        self.assertEqual(response.status_code, 200)
