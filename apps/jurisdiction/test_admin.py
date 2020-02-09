from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from .models import Jurisdiction, State


class JurisdictionAdminTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'admin@api.work.vote', 'passwd')
        self.client = Client()
        self.assertTrue(self.client.login(username='admin', password='passwd'))

    def test_fields(self):
        ca = State.objects.create(name='California')
        sf = Jurisdiction.objects.create(name='San Francisco', state=ca)
        response = self.client.get('/admin/jurisdiction/jurisdiction/%d/' % sf.id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Jurisdiction Name:')
        self.assertNotContains(response, 'candidate_prohibition')
