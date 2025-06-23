from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from flights.models import Flight

class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = 'P', _('Pending')
        CONFIRMED = 'C', _('Confirmed')
        CANCELLED = 'X', _('Cancelled')
    
    class TravelClass(models.TextChoices):
        ECONOMY = 'E', _('Economy')
        BUSINESS = 'B', _('Business')
        FIRST = 'F', _('First Class')
    
    booking_reference = models.CharField(max_length=8, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    travel_class = models.CharField(max_length=1, choices=TravelClass.choices)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.PENDING)
    seats = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.booking_reference:
            self.booking_reference = self._generate_reference()
        super().save(*args, **kwargs)
    
    def _generate_reference(self):
        import random
        import string
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    
    def __str__(self):
        return self.booking_reference