from django.contrib import admin

from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'service', 'status', 'preferred_date', 'created_at')
    list_editable = ('status',)
    list_filter = ('status', 'service', 'preferred_date')
    search_fields = ('full_name', 'email', 'phone', 'address')
    list_select_related = ('service',)
    readonly_fields = ('privacy_consent', 'consent_given_at', 'created_at', 'updated_at')
    fieldsets = (
        ('Management', {'fields': ('status', 'internal_notes')}),
        ('Customer', {'fields': ('full_name', 'email', 'phone')}),
        ('Job', {'fields': ('service', 'preferred_date', 'preferred_time', 'description')}),
        ('Property', {'fields': ('address', 'property_type')}),
        ('System', {'fields': ('privacy_consent', 'consent_given_at', 'created_at', 'updated_at')}),
    )