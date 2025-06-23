from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from flights.models import Flight
from .models import Booking
from .forms import BookingForm

@login_required
def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.flight = flight
            booking.save()
            return redirect('booking_confirmation', booking_reference=booking.booking_reference)
    else:
        form = BookingForm(initial={
            'travel_class': request.GET.get('class', 'E'),
            'seats': request.GET.get('passengers', 1)
        })
    
    return render(request, 'bookings/create.html', {
        'flight': flight,
        'form': form
    })

@login_required
def booking_confirmation(request, booking_reference):
    booking = get_object_or_404(Booking, booking_reference=booking_reference, user=request.user)
    return render(request, 'bookings/confirmation.html', {'booking': booking})