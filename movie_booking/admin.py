from django.contrib import admin
from .models import Movie, Screen, Booking, FoodItem

# Register your models here.

admin.site.register(Movie)
admin.site.register(Screen)
admin.site.register(Booking)
admin.site.register(FoodItem)
