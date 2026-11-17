def business(request):
    """Shared HomeFix business information for all templates."""
    return {
        'business': {
            'name': 'HomeFix',
            'tagline': 'Reliable home repairs and maintenance.',
            'phone': '(555) 010-0199',
            'email': 'hello@homefix.example',
            'hours': 'Monday to Saturday, 8am to 6pm',
            'service_areas': [
                'Downtown',
                'North side',
                'South side',
                'West end',
                'East side',
                'Nearby suburbs',
            ],
        }
    }