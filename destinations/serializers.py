

from rest_framework import serializers
from destinations.models import Destination, DestinationImage, WelcomeDestination
import logging



logger = logging.getLogger(__name__)
class DestinationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DestinationImage
        fields = ['image']

class DestinationListSerializer(serializers.ModelSerializer):
    images = DestinationImageSerializer(many=True, required=True)

    class Meta:
        model = Destination
        fields = ['id', 'name', 'description', 'location', 'latitude', 'longitude', 'average_rating', 'created_at', 'updated_at', 'images']    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = [image.image.url for image in instance.images.all()]
        return representation
    

class DestinationCreateSerializer(serializers.ModelSerializer):
    print("Inside DestinationCreateSerializer")
    images = DestinationImageSerializer(many=True, required=True)
    class Meta:
        model = Destination
        fields = '__all__'


    def create(self, validated_data):
        logger.debug("Inside create method with validated data: %s", validated_data)
        images_data = validated_data.pop('images')
        destination = Destination.objects.create(**validated_data)

        for image_data in images_data:
            DestinationImage.objects.create(destination=destination, **image_data)
        
        logger.debug("Destination created: %s", destination)
        return destination
    

class WelcomeDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelcomeDestination
        fields = '__all__'