from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    appointment_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Appointment
        fields = ['provider_name', 'appointment_time', 'client_email']
