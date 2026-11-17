from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', TemplateView.as_view(
        template_name='core/about.html'
    ), name='about'),
    path('contact/', TemplateView.as_view(
        template_name='core/contact.html'
    ), name='contact'),
    path('privacy/', TemplateView.as_view(
        template_name='core/privacy.html'
    ), name='privacy'),
]