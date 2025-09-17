from rest_framework import serializers
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from cabinet.models import Doctor,Schedule, Appointment

class DoctorListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'date_created', 'date_updated', 'name','speciality','active']

class DoctorDetailSerializer(serializers.ModelSerializer):

    schedules = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'date_created', 'date_updated', 'name', 'schedules']
    def get_schedules(self, instance):
        queryset = instance.schedules.filter(active=True)
        serializer = ScheduleListSerializer(queryset, many=True)
        return serializer.data


class ScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'day_ofduty', 'from_hour','doctor']

class ScheduleDetailSerializer(serializers.ModelSerializer):

    appointments = serializers.SerializerMethodField()
    from_hour=serializers.TimeField(format="%H:%M:%S")
    class Meta:
        model = Schedule
        fields = ['id', 'from_hour', 'day_ofduty', 'from_hour', 'appointments']

    def get_appointments(self, instance):
        queryset = instance.appointments.filter(active=True)
        serializer = AppointmentSerializer(queryset, many=True)
        return serializer.data
        
class AppointmentListSerializer(serializers.ModelSerializer):
    date_created=serializers.DateTimeField(format="%A %Y-%m-%d %H:%M:%S")
    date_updated=serializers.DateTimeField(format="%A %Y-%m-%d %H:%M:%S")
    class Meta:
        model = Appointment
        fields = ['id', 'date_created', 'date_updated', 'patient_name', 'price', 'schedule']


