from django.db import models
# from django.contrib.auth import get_user_model

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Destinations'
        ordering = ['name']

    def __str__(self):
        return self.name


class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='destination_images/')
    
    def __str__(self):
        return f"{self.destination.name} Image"
    


# welcome page destination model
class WelcomeDestination(models.Model):
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='welcome_destination_images/')

    def __str__(self):
        return self.title

# class Review(models.Model):
#     destination = models.ForeignKey(Destination, related_name='reviews', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1 to 5 rating system
#     comment = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Review by {self.user} for {self.destination.name}"