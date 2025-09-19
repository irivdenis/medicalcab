from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponse
from cabinet.models import Doctor, Schedule, Appointment
from cabinet.forms import DoctorForm,AppointmentForm,ScheduleForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'cabinet/all_doctors.html',
                  {'doctors':doctors})
def schedule_list(request):
    items = Schedule.objects.all()
    return render(request, 'cabinet/all_schedules.html',
                  {'items':items})
def appointment_list(request):
    items = Appointment.objects.all()
    return render(request, 'cabinet/all_appointments.html',
                  {'items':items})
                  
                  
@login_required
def doctor_detail(request, id):  
   doctor=Doctor.objects.get(id=id)
   return render(request,
          'cabinet/detail_doctor.html',
            {'doctor':doctor}) # nous passons l'id au modèle 

def schedule_detail(request, id):  
   schedule=Schedule.objects.get(id=id)
   return render(request,
          'cabinet/detail_schedule.html',
            {'schedule':schedule}) # nous passons l'id au modèle 

def appointment_detail(request, id):  
   appointment=Appointment.objects.get(id=id)
   return render(request,
          'cabinet/detail_appointment.html',
            {'appointment':appointment}) # nous passons l'id au modèle 

@login_required
def home(request):
    return render(request, 'cabinet/home.html')
    
def addnew_doctor(request):
    form = DoctorForm()
      
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():

            doctor = form.save()

            return redirect('doctors-list')

        else:
            form = DoctorForm()
            
    return render(request, 'cabinet/newdoctor.html',{'form': form})
    
def addnew_schedule(request):
    form = ScheduleForm()
      
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():

            schedule = form.save()

            return redirect('schedules-list')

        else:
            form = ScheduleForm()
            
    return render(request, 'cabinet/newschedule.html',{'form': form})
    
def page1(request):
    if request.method=="GET":
        return HttpResponse ("<h2>La page n'est pas disponible , contactez l'administrateur<h2>")
        
def update_Doctormodel(request, id):
    instance = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            # Redirect to a success page or the detail view of the updated object
            return redirect('doctors-list')
    else:
        form = DoctorForm(instance=instance)
    return render(request, 'cabinet/update_doctor.html', {'form': form})
      
def addnew_appointment(request):
    form = AppointmentForm()
      
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():

            appointment = form.save()

            return redirect('appointments-list')

        else:
            form = AppointmentForm()
    schedule = Schedule.objects.get(id=id)

            
    return render(request, 'cabinet/newappointment.html',{'form': form})
    
def update_schedule(request, id):
    instance=Schedule.objects.get(id=id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('schedule-detail', id=schedule.id)
    else:
        form = ScheduleForm(instance=instance)

    return render(request,
                'cabinet/update_schedule.html',
                {'form': form})

    
def update_doctor(request, id):
    doctor = Doctor.objects.get(id=id)

    if request.method == 'POST':
        form = Doctor(request.POST, instance=doctor)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('doctor-detail',doctor.id)
    else:
        form = DoctorForm(instance=doctor)

    return render(request,
                'cabinet/update_doctor.html',
                {'form': form})

def update_appointment(request, id):
    instance=Appointment.objects.get(id=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('schedule-detail', id=appointment.id)
    else:
        form = AppointmentForm(instance=instance)

    return render(request,
                'cabinet/update_appointment.html',
                {'form': form})


