from django.contrib import admin
from .models import Airport, Flight, Airline

# Register your models here.
admin.site.register(Airport, Flight, Airline)