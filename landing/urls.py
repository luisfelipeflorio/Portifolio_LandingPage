from django.urls import path
from .views import LandingPageView, ThankYouView, LeadCreateView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('lead-create/', LeadCreateView.as_view(), name='lead_create'),
    path('obrigado/', ThankYouView.as_view(), name='thank_you'),
]
