 
from django.urls import path
from destinations.views import DestinationListAPIView, DestinationListCreateAPIView, PopularDestinationsView, WelcomeDestinationView




urlpatterns = [
    path('list/', DestinationListAPIView.as_view(), name='destinations'),
    path('create/', DestinationListCreateAPIView.as_view(), name='create'),
    path('popular-destinations/', PopularDestinationsView.as_view(), name='popular-destinations'),
    path('welcome-destinations/', WelcomeDestinationView.as_view(), name='welcome-destinations'),
]