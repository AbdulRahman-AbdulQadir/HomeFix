import re
from datetime import timedelta

from django import forms
from django.utils import timezone

from services.models import Service

from .models import ServiceRequest


class ServiceRequestForm(forms.ModelForm):
    privacy_consent = forms.BooleanField(
        required=True,
        error_messages={'required': 'Please agree to the privacy policy to send your request.'},
    )
    # Honeypot: real visitors never see or fill this field; bots often do.
    website = forms.CharField(required=False)

    class Meta:
        model = ServiceRequest
        fields = [
            'full_name', 'email', 'phone', 'service', 'preferred_date',
            'preferred_time', 'description', 'address', 'property_type',
        ]
        labels = {
            'full_name': 'Full name',
            'phone': 'Phone number',
            'preferred_date': 'Preferred date',
            'preferred_time': 'Preferred time',
            'description': 'Describe the job (optional)',
            'address': 'Property address',
            'property_type': 'Property type',
        }
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)
        self.fields['service'].empty_label = 'Choose a service'
        self.fields['property_type'].choices = (
            [('', 'Choose property type')] + list(ServiceRequest.PropertyType.choices)
        )
        self.fields['preferred_date'].widget.attrs['min'] = timezone.localdate().isoformat()
        self.fields['website'].widget.attrs.update({'tabindex': '-1', 'autocomplete': 'off'})
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-check' if name == 'privacy_consent' else 'form-input'

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()
        digits = re.sub(r'\D', '', phone)
        if not re.fullmatch(r'\+?[0-9\s().-]+', phone) or not 7 <= len(digits) <= 15:
            raise forms.ValidationError('Enter a valid phone number, for example 555-010-0199.')
        return phone

    def clean_preferred_date(self):
        date = self.cleaned_data['preferred_date']
        if date < timezone.localdate():
            raise forms.ValidationError('Please choose today or a future date.')
        return date

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get('email')
        service = cleaned.get('service')
        date = cleaned.get('preferred_date')
        if email and service and date:
            since = timezone.now() - timedelta(hours=24)
            if ServiceRequest.objects.filter(
                email__iexact=email, service=service,
                preferred_date=date, created_at__gte=since,
            ).exists():
                raise forms.ValidationError(
                    'It looks like you already sent this request. We have it and will be in touch.'
                )
        return cleaned

    def save(self, commit=True):
        request_obj = super().save(commit=False)
        request_obj.privacy_consent = True
        request_obj.consent_given_at = timezone.now()
        if commit:
            request_obj.save()
        return request_obj