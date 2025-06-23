from django.db import models
from django.utils.translation import gettext_lazy as _

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Airline(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='airlines/', blank=True)
    
    def __str__(self):
        return self.name

class Flight(models.Model):
    class Status(models.TextChoices):
        SCHEDULED = 'S', _('Scheduled')
        DELAYED = 'D', _('Delayed')
        CANCELLED = 'C', _('Cancelled')
        COMPLETED = 'F', _('Completed')
    
    flight_number = models.CharField(max_length=10)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, related_name='departures', on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey(Airport, related_name='arrivals', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.DurationField()
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.SCHEDULED)
    economy_seats = models.PositiveIntegerField()
    business_seats = models.PositiveIntegerField()
    first_class_seats = models.PositiveIntegerField()
    economy_price = models.DecimalField(max_digits=10, decimal_places=2)
    business_price = models.DecimalField(max_digits=10, decimal_places=2)
    first_class_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.airline.code}{self.flight_number}"