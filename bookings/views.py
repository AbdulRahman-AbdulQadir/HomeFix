from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from services.models import Service

from .forms import ServiceRequestForm
from .models import ServiceRequest


class RequestCreateView(FormView):
    template_name = 'bookings/request_form.html'
    form_class = ServiceRequestForm
    success_url = reverse_lazy('bookings:received')

    def get_initial(self):
        initial = super().get_initial()
        slug = self.request.GET.get('service')
        if slug:
            service = Service.objects.filter(slug=slug, is_active=True).first()
            if service:
                initial['service'] = service
        return initial

    def form_valid(self, form):
        if form.cleaned_data.get('website'):
            # Honeypot filled in: act as if it worked, but save nothing.
            return HttpResponseRedirect(self.get_success_url())
        service_request = form.save()
        self.request.session['last_request_id'] = service_request.pk
        return HttpResponseRedirect(self.get_success_url())


class RequestReceivedView(TemplateView):
    template_name = 'bookings/request_received.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request_id'] = self.request.session.get('last_request_id')
        return context

@staff_member_required
def dashboard(request):
    """Simple staff-only overview of request activity."""
    Status = ServiceRequest.Status
    stats = ServiceRequest.objects.aggregate(
        total=Count('id'),
        pending=Count('id', filter=Q(status=Status.PENDING)),
        scheduled=Count('id', filter=Q(status=Status.SCHEDULED)),
        completed=Count('id', filter=Q(status=Status.COMPLETED)),
    )
    recent = ServiceRequest.objects.select_related('service')[:5]
    return render(request, 'bookings/dashboard.html', {'stats': stats, 'recent': recent})