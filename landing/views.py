from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Testimonial, FAQ, Lead
from .forms import LeadForm

class LandingPageView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.filter(is_active=True)
        context['faqs'] = FAQ.objects.filter(is_active=True)
        context['form'] = LeadForm()
        return context

class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'landing/index.html'
    success_url = reverse_lazy('thank_you')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.filter(is_active=True)
        context['faqs'] = FAQ.objects.filter(is_active=True)
        return context

class ThankYouView(TemplateView):
    template_name = 'landing/thank_you.html'
