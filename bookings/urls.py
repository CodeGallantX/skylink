from django.urls import path
from . import views

urlpatterns = [
    path('new/<int:flight_id>/', views.create_booking, name='create_booking'),
    path('confirmation/<str:booking_reference>/', views.booking_confirmation, name='booking_confirmation'),
]