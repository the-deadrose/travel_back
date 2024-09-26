
from django.urls import path, include

urlpatterns = [
    path('destination/', include('destinations.urls')),
]