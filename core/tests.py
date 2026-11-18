from django.template.loader import render_to_string
from django.test import TestCase, override_settings
from django.urls import reverse


class PublicPageTests(TestCase):
    def test_public_pages_load(self):
        for name in ('core:home', 'core:about', 'core:contact', 'core:privacy',
                     'services:list', 'bookings:request'):
            with self.subTest(page=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 200)

    def test_homepage_labels_testimonials_as_demo_content(self):
        self.assertContains(self.client.get(reverse('core:home')), 'not real customer reviews')


class ErrorPageTests(TestCase):
    @override_settings(DEBUG=False)
    def test_custom_404_page(self):
        response = self.client.get('/this-page-does-not-exist/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Page not found', status_code=404)

    def test_500_template_renders(self):
        self.assertIn('Something went wrong', render_to_string('500.html'))