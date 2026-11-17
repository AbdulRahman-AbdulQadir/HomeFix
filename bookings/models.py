from django.db import models


class ServiceRequest(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        REVIEWING = 'reviewing', 'Reviewing'
        CONTACTED = 'contacted', 'Contacted'
        SCHEDULED = 'scheduled', 'Scheduled'
        IN_PROGRESS = 'in_progress', 'In progress'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'
        DECLINED = 'declined', 'Declined'

    class PreferredTime(models.TextChoices):
        MORNING = 'morning', 'Morning'
        AFTERNOON = 'afternoon', 'Afternoon'
        EVENING = 'evening', 'Evening'
        FLEXIBLE = 'flexible', 'Flexible'

    class PropertyType(models.TextChoices):
        HOUSE = 'house', 'House'
        TOWNHOUSE = 'townhouse', 'Townhouse'
        CONDO = 'condo', 'Condo or apartment'
        OTHER = 'other', 'Other'

    # Customer
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30)

    # Job
    service = models.ForeignKey(
        'services.Service', on_delete=models.PROTECT, related_name='requests'
    )
    preferred_date = models.DateField()
    preferred_time = models.CharField(
        max_length=20, choices=PreferredTime.choices, default=PreferredTime.FLEXIBLE
    )
    description = models.TextField(blank=True)

    # Property
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PropertyType.choices)

    # Consent
    privacy_consent = models.BooleanField(default=False)
    consent_given_at = models.DateTimeField(null=True, blank=True)

    # Management
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING, db_index=True
    )
    internal_notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'#{self.pk} {self.full_name} - {self.service}'