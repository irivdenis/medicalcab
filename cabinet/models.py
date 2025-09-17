from django.db import models

# Create your models here.


class Doctor(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    speciality = models.TextField(blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Schedule(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    day_ofduty = models.CharField(max_length=20)
    from_hour= models.TimeField(blank=True, null=True) # Optional field
    end_hour= models.TimeField(blank=True, null=True) # Optional field
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    doctor = models.ForeignKey('cabinet.Doctor', on_delete=models.CASCADE, related_name='schedules')

    def __str__(self):
        return self.doctor.speciality+': '+ self.doctor.name


class Appointment(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    patient_name = models.CharField(max_length=80)
    gender = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.ForeignKey('cabinet.Schedule', on_delete=models.CASCADE, related_name='appointments')
    appoint_date= models.DateTimeField()
    def __str__(self):
        return self.patient_name
