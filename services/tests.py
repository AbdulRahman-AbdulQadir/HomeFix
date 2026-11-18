from io import StringIO

from django.core.management import call_command
from django.db.models import ProtectedError
from django.test import TestCase
from django.urls import reverse

from bookings.models import ServiceRequest

from .models import Service


class ServicePageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.active = Service.objects.create(
            name='Active one', slug='active-one', short_description='s', description='d'
        )
        cls.hidden = Service.objects.create(
            name='Hidden one', slug='hidden-one', short_description='s', description='d', is_active=False
        )

    def test_list_shows_only_active_services(self):
        response = self.client.get(reverse('services:list'))
        self.assertContains(response, 'Active one')
        self.assertNotContains(response, 'Hidden one')

    def test_detail_of_active_service_loads(self):
        response = self.client.get(reverse('services:detail', args=['active-one']))
        self.assertEqual(response.status_code, 200)

    def test_detail_of_inactive_service_is_404(self):
        response = self.client.get(reverse('services:detail', args=['hidden-one']))
        self.assertEqual(response.status_code, 404)

    def test_service_with_requests_cannot_be_deleted(self):
        ServiceRequest.objects.create(
            full_name='A', email='a@example.com', phone='555-0100', service=self.active,
            preferred_date='2030-01-01', address='x', property_type='house',
        )
        with self.assertRaises(ProtectedError):
            self.active.delete()


class SeedDemoTests(TestCase):
    def test_seed_is_safe_to_run_twice(self):
        for _ in range(2):
            call_command('seed_demo', stdout=StringIO())
        self.assertEqual(Service.objects.count(), 6)
        self.assertEqual(ServiceRequest.objects.count(), 4)