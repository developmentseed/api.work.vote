from django.test import TestCase
from django.test import Client
from jurisdiction.models import Jurisdiction, State


class JurisdictionViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_jurisdiction_view(self):
        ca = State.objects.create(name='California')
        sf = Jurisdiction.objects.create(name='San Francisco', state=ca)
        response = self.client.get('/jurisdictions/%d/' % sf.id)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'San Francisco County')

    def test_missing_jurisdiction(self):
        response = self.client.get('/jurisdictions/42/')
        self.assertEqual(response.status_code, 404)
        
    def test_jurisdiction_geojson_view_no_geometry(self):
        ca = State.objects.create(name='California')
        sf = Jurisdiction.objects.create(name='San Francisco', state=ca)
        response = self.client.get('/jurisdictions/%d/geojson/' % sf.id)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.content)
