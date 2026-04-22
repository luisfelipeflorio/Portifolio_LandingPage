from django.urls import path
from .views import LandingPageView, ThankYouView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('obrigado/', ThankYouView.as_view(), name='thank_you'),
]
