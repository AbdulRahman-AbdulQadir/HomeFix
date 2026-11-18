from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from services.models import Service

from .forms import ServiceRequestForm
from .models import ServiceRequest


def make_service(slug='general-repairs', active=True):
    return Service.objects.create(
        name=slug.title(), slug=slug, short_description='Short', description='Long', is_active=active
    )


def valid_data(service, **overrides):
    data = {
        'full_name': 'Test User', 'email': 'test@example.com', 'phone': '780-555-0123',
        'service': service.pk,
        'preferred_date': (timezone.localdate() + timedelta(days=3)).isoformat(),
        'preferred_time': 'morning', 'address': '1 Test Street', 'property_type': 'house',
        'description': '', 'privacy_consent': 'on', 'website': '',
    }
    data.update(overrides)
    return data


def make_request(service, status='pending', email='a@example.com'):
    return ServiceRequest.objects.create(
        full_name='A Customer', email=email, phone='555-0100', service=service,
        preferred_date=timezone.localdate() + timedelta(days=2), address='1 Test Street',
        property_type='house', status=status, privacy_consent=True,
    )


class ServiceRequestModelTests(TestCase):
    def test_new_request_defaults_to_pending(self):
        obj = make_request(make_service())
        self.assertEqual(obj.status, ServiceRequest.Status.PENDING)

    def test_str_contains_name_and_service(self):
        obj = make_request(make_service())
        self.assertIn('A Customer', str(obj))


class ServiceRequestFormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = make_service()

    def test_valid_form(self):
        self.assertTrue(ServiceRequestForm(valid_data(self.service)).is_valid())

    def test_past_date_rejected(self):
        past = (timezone.localdate() - timedelta(days=1)).isoformat()
        form = ServiceRequestForm(valid_data(self.service, preferred_date=past))
        self.assertIn('preferred_date', form.errors)

    def test_consent_required(self):
        form = ServiceRequestForm(valid_data(self.service, privacy_consent=''))
        self.assertIn('privacy_consent', form.errors)

    def test_invalid_phone_rejected(self):
        form = ServiceRequestForm(valid_data(self.service, phone='abc'))
        self.assertIn('phone', form.errors)

    def test_invalid_email_rejected(self):
        form = ServiceRequestForm(valid_data(self.service, email='nope'))
        self.assertIn('email', form.errors)

    def test_inactive_service_not_selectable(self):
        old = make_service('old-service', active=False)
        form = ServiceRequestForm(valid_data(old))
        self.assertIn('service', form.errors)

    def test_save_records_consent(self):
        form = ServiceRequestForm(valid_data(self.service))
        self.assertTrue(form.is_valid())
        obj = form.save()
        self.assertTrue(obj.privacy_consent)
        self.assertIsNotNone(obj.consent_given_at)

    def test_duplicate_within_24_hours_rejected(self):
        first = ServiceRequestForm(valid_data(self.service))
        first.is_valid()
        first.save()
        second = ServiceRequestForm(valid_data(self.service))
        self.assertFalse(second.is_valid())
        self.assertTrue(second.non_field_errors())


class RequestViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.service = make_service()

    def test_form_page_loads(self):
        self.assertEqual(self.client.get(reverse('bookings:request')).status_code, 200)

    def test_service_prefilled_from_query_string(self):
        response = self.client.get(reverse('bookings:request') + f'?service={self.service.slug}')
        self.assertEqual(response.context['form'].initial['service'], self.service)

    def test_valid_post_creates_pending_request(self):
        response = self.client.post(reverse('bookings:request'), valid_data(self.service))
        self.assertRedirects(response, reverse('bookings:received'))
        obj = ServiceRequest.objects.get()
        self.assertEqual(obj.status, ServiceRequest.Status.PENDING)

    def test_confirmation_says_not_a_confirmed_appointment(self):
        response = self.client.post(reverse('bookings:request'), valid_data(self.service), follow=True)
        self.assertContains(response, 'not a confirmed appointment')

    def test_invalid_post_saves_nothing(self):
        response = self.client.post(reverse('bookings:request'), valid_data(self.service, phone='abc'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ServiceRequest.objects.count(), 0)

    def test_honeypot_saves_nothing(self):
        response = self.client.post(reverse('bookings:request'), valid_data(self.service, website='spam.example'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ServiceRequest.objects.count(), 0)


class DashboardTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.staff = User.objects.create_user('staff', password='pw', is_staff=True)
        cls.customer = User.objects.create_user('customer', password='pw')
        service = make_service()
        make_request(service, 'pending', 'a@example.com')
        make_request(service, 'pending', 'b@example.com')
        make_request(service, 'scheduled', 'c@example.com')
        make_request(service, 'completed', 'd@example.com')

    def test_anonymous_redirected_to_login(self):
        response = self.client.get(reverse('bookings:dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)

    def test_non_staff_redirected(self):
        self.client.force_login(self.customer)
        self.assertEqual(self.client.get(reverse('bookings:dashboard')).status_code, 302)

    def test_staff_sees_correct_numbers(self):
        self.client.force_login(self.staff)
        response = self.client.get(reverse('bookings:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['stats'],
            {'total': 4, 'pending': 2, 'scheduled': 1, 'completed': 1},
        )


class AdminTests(TestCase):
    def test_admin_pages_load_for_superuser(self):
        get_user_model().objects.create_superuser('boss', 'b@example.com', 'pw')
        self.client.login(username='boss', password='pw')
        obj = make_request(make_service())
        for url in (
            reverse('admin:bookings_servicerequest_changelist'),
            reverse('admin:bookings_servicerequest_change', args=[obj.pk]),
            reverse('admin:services_service_changelist'),
        ):
            self.assertEqual(self.client.get(url).status_code, 200, url)