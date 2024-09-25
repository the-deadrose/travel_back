from django.contrib import admin

from destinations.models import Destination, DestinationImage, WelcomeDestination

# Register your models here.
admin.site.register(Destination)
admin.site.register(DestinationImage)
admin.site.register(WelcomeDestination)
