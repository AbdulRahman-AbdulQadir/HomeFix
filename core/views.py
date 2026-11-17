from django.shortcuts import render

from django.views.generic import TemplateView

from services.models import Service


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(
            is_active=True
        )[:6]
        return context