from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Movie, Screen, Booking

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    return render(request, 'movies_booking/home.html', {'movies': movies})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'movies_booking/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'movies_booking/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def book(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    screens = Screen.objects.filter(movie=movie)
    if request.method == 'POST':
        screen_id = request.POST['screen_id']
        seats = request.POST['seats']
        screen = get_object_or_404(Screen, id=screen_id)
        booking = Booking(user=request.user, screen=screen, seats=seats)
        booking.save()
        return redirect('confirmation', booking_id=booking.id)
    return render(request, 'movies_booking/booking.html', {'movie': movie, 'screens': screens})

@login_required
def confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'movies_booking/confirmation.html', {'booking': booking})