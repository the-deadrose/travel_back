 
from django.urls import path
from destinations.views import DestinationView, DestinationImageView, PopularDestinationsView




urlpatterns = [
    path('destinations/', DestinationView.as_view(), name='destinations'),
    path('destination-images/', DestinationImageView.as_view(), name='destination-images'),
    path('popular-destinations/', PopularDestinationsView.as_view(), name='popular-destinations'),
]