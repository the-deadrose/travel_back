from django.shortcuts import render
from destinations.models import Destination, DestinationImage, WelcomeDestination
from destinations.serializers import DestinationSerializer, DestinationImageSerializer, WelcomeDestinationSerializer
from travel_back.pagination import CustomPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# Create your views here.
class DestinationView(ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = Destination.objects.all().order_by('-average_rating')[:5]
        return queryset

class DestinationImageView(ListAPIView):
    queryset = DestinationImage.objects.all()
    serializer_class = DestinationImageSerializer



class PopularDestinationsView(ListAPIView):
    queryset = Destination.objects.all().order_by('-average_rating')[:5]
    serializer_class = DestinationSerializer
    pagination_class = CustomPagination


class WelcomeDestinationView(ListAPIView):
    serializer_class = WelcomeDestinationSerializer

    # get with out pagination
    def get_queryset(self):
        queryset = WelcomeDestination.objects.all()
        return queryset