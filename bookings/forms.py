from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    TRAVEL_CLASS_CHOICES = [
        ('E', 'Economy'),
        ('B', 'Business'),
        ('F', 'First Class'),
    ]
    
    travel_class = forms.ChoiceField(
        choices=TRAVEL_CLASS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        initial='E'
    )
    
    seats = forms.IntegerField(
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '1',
            'max': '10'
        })
    )
    
    passenger_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    passenger_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    
    passenger_phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['travel_class', 'seats', 'passenger_name', 'passenger_email', 'passenger_phone']
        
    def clean_seats(self):
        seats = self.cleaned_data.get('seats')
        if seats < 1:
            raise forms.ValidationError("You must book at least 1 seat.")
        return seats
    
    def clean(self):
        cleaned_data = super().clean()
        travel_class = cleaned_data.get('travel_class')
        seats = cleaned_data.get('seats')
        
        # You can add additional validation here based on flight availability
        # For example, check if there are enough seats in the selected class
        
        return cleaned_data