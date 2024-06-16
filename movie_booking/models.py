from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    showtimes = models.TextField() 

    def __str__(self):
        return self.title

class Screen(models.Model):
    screen_number = models.IntegerField()
    seat_count = models.IntegerField(default=60)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Screen {self.screen_number} - {self.movie.title}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seats = models.TextField() 
    booking_time = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name