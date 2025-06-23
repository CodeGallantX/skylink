from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.flight_search, name='flight_search'),
]