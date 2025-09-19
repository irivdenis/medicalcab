from django import forms
from cabinet.models import Doctor, Appointment, Schedule

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor

        fields = '__all__'
        
class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = '__all__'
        
class ScheduleForm(forms.ModelForm):

    class Meta:
        model = Schedule

        fields = '__all__'
