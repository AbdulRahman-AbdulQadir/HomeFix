from datetime import date, timedelta

from django.core.management.base import BaseCommand

from bookings.models import ServiceRequest
from services.models import Service

SERVICES = [
    ('General household repairs', 'general-repairs', 'wrench',
     'Fixes for the small and medium problems around your home.',
     'From squeaky hinges to loose handrails, we handle the everyday repairs that make a home feel looked after.'),
    ('Furniture assembly', 'furniture-assembly', 'armchair',
     'Flat-pack furniture built correctly and safely.',
     'Beds, wardrobes, desks and shelving assembled properly, so they are sturdy and ready to use.'),
    ('Painting and minor improvements', 'painting-improvements', 'paint-roller',
     'Neat painting and small upgrades that refresh a room.',
     'Touch-ups, single rooms and small improvement jobs finished cleanly, with floors and furniture protected.'),
    ('Door, cabinet, and fixture repairs', 'door-cabinet-fixtures', 'door-open',
     'Doors, cabinets and fixtures that open, close and hold properly.',
     'We adjust, repair or replace hinges, handles, latches and fittings so everything works smoothly again.'),
    ('Home installations', 'home-installations', 'drill',
     'Shelves, TV mounts, curtain rods and similar installations.',
     'Secure, level installations of everyday household items, fixed into the right wall type.'),
    ('Basic property maintenance', 'property-maintenance', 'home',
     'Regular upkeep to keep your property in good shape.',
     'Seasonal checks and routine tasks that prevent small issues from becoming expensive ones.'),
]

REQUESTS = [
    ('Maya Demo', 'maya.demo@example.com', 'general-repairs', 'pending', 5),
    ('Liam Demo', 'liam.demo@example.com', 'furniture-assembly', 'reviewing', 7),
    ('Noor Demo', 'noor.demo@example.com', 'painting-improvements', 'scheduled', 10),
    ('Omar Demo', 'omar.demo@example.com', 'home-installations', 'completed', -3),
]


class Command(BaseCommand):
    help = 'Create or refresh demonstration services and requests (safe to run repeatedly).'

    def handle(self, *args, **options):
        for order, (name, slug, icon, short, long) in enumerate(SERVICES, start=1):
            Service.objects.update_or_create(
                slug=slug,
                defaults={'name': name, 'icon': icon, 'short_description': short,
                          'description': long, 'display_order': order, 'is_active': True},
            )
        for full_name, email, slug, status, days in REQUESTS:
            ServiceRequest.objects.get_or_create(
                email=email,
                defaults={
                    'full_name': full_name, 'phone': '555-0100',
                    'service': Service.objects.get(slug=slug),
                    'preferred_date': date.today() + timedelta(days=days),
                    'address': '123 Demo Street', 'property_type': 'house',
                    'status': status, 'privacy_consent': True,
                    'description': 'Demonstration request.',
                },
            )
        self.stdout.write(self.style.SUCCESS('Demo data ready.'))