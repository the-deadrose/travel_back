 
from django.urls import path
from destinations.views import DestinationListAPIView, DestinationListCreateAPIView, InspirationDestinationView, PopularDestinationsView, WelcomeDestinationView




urlpatterns = [
    path('list/', DestinationListAPIView.as_view(), name='destinations'),
    path('create/', DestinationListCreateAPIView.as_view(), name='create'),
    path('popular/', PopularDestinationsView.as_view(), name='popular'),
    path('welcome/', WelcomeDestinationView.as_view(), name='welcome'),
    path ('inspiration/', InspirationDestinationView.as_view(), name='inspiration')
]