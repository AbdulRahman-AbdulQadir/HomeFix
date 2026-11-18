from django.urls import path

from .views import RequestCreateView, RequestReceivedView, dashboard

app_name = 'bookings'

urlpatterns = [
    path('request/', RequestCreateView.as_view(), name='request'),
    path('request/received/', RequestReceivedView.as_view(), name='received'),
    path('dashboard/', dashboard, name='dashboard'),
]