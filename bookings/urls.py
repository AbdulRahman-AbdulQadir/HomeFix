from django.urls import path
from django.views.generic import TemplateView

app_name = 'bookings'

urlpatterns = [
    path(
        'request/',
        TemplateView.as_view(template_name='bookings/request.html'),
        name='request',
    ),
]