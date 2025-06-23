from django.shortcuts import render
from django.db.models import Q
from datetime import datetime, timedelta
from .models import Flight, Airport

def flight_search(request):
    airports = Airport.objects.all()
    
    if request.method == 'GET':
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        departure_date = request.GET.get('departure_date')
        passengers = int(request.GET.get('passengers', 1))
        travel_class = request.GET.get('class', 'economy')
        
        if all([origin, destination, departure_date]):
            try:
                departure_date = datetime.strptime(departure_date, '%Y-%m-%d').date()
                next_day = departure_date + timedelta(days=1)
                
                flights = Flight.objects.filter(
                    departure_airport__code=origin,
                    arrival_airport__code=destination,
                    departure_time__date__range=[departure_date, next_day],
                    status='S'
                ).order_by('departure_time')
                
                return render(request, 'flights/results.html', {
                    'flights': flights,
                    'search_params': request.GET,
                    'airports': airports
                })
            except Exception as e:
                return render(request, 'flights/search.html', {
                    'error': str(e),
                    'airports': airports
                })
    
    return render(request, 'flights/search.html', {'airports': airports})