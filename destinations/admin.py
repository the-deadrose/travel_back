from django.contrib import admin

from destinations.models import Destination, DestinationImage

# Register your models here.
admin.site.register(Destination)
admin.site.register(DestinationImage)
