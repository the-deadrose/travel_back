

from rest_framework import serializers
from destinations.models import Destination, DestinationImage, WelcomeDestination


class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = ['id', 'image', 'uploaded_at']



class DestinationSerializer(serializers.ModelSerializer):
    images = DestinationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'description', 'location', 'latitude', 'longitude', 'average_rating', 'created_at', 'updated_at', 'images']

class WelcomeDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeDestination
        fields = '__all__'