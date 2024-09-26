from django.shortcuts import render
from destinations.models import Destination, DestinationImage, WelcomeDestination
from destinations.serializers import DestinationCreateSerializer, DestinationListSerializer, WelcomeDestinationSerializer
from travel_back.pagination import CustomPagination
from rest_framework.generics import ListAPIView 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status

# Create your views here.

class DestinationListAPIView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationListSerializer




class DestinationListCreateAPIView(generics.CreateAPIView):
    print("Inside DestinationListCreateAPIView")
    queryset = Destination.objects.all()
    serializer_class = DestinationCreateSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return self.perform_create(serializer)
        else:
            print("Validation errors:", serializer.errors)  # Print validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    

 


class PopularDestinationsView(ListAPIView):
    queryset = Destination.objects.all().order_by('-average_rating')[:5]
    serializer_class = DestinationListSerializer
    pagination_class = CustomPagination


class WelcomeDestinationView(ListAPIView):
    serializer_class = WelcomeDestinationSerializer

    # get with out pagination
    def get_queryset(self):
        queryset = WelcomeDestination.objects.all()
        return queryset
    





class InspirationDestinationView(ListAPIView):
    serializer_class = DestinationListSerializer

    def get_queryset(self):
        queryset = Destination.objects.order_by('?')[:5]
        return queryset