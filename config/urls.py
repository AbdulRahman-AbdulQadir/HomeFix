from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('services/', include('services.urls')),
    path('', include('bookings.urls')),
    path('', include('core.urls')),
]