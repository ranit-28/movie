from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('booking/<int:movie_id>/', views.book, name='book'),
    path('confirmation/<int:booking_id>/', views.confirmation, name='confirmation'),
]