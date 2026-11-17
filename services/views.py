from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Service


class ServiceListView(ListView):
    queryset = Service.objects.filter(is_active=True)
    context_object_name = 'services'
    template_name = 'services/service_list.html'


class ServiceDetailView(DetailView):
    queryset = Service.objects.filter(is_active=True)
    context_object_name = 'service'
    template_name = 'services/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['other_services'] = (
            Service.objects.filter(is_active=True)
            .exclude(pk=self.object.pk)[:3]
        )
        return context
