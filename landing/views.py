from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'landing/index.html'

class ThankYouView(TemplateView):
    template_name = 'landing/thank_you.html'
