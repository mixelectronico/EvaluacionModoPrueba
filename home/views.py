from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import User
from home.models import Appointment


# Create your views here.
def home(request):
    reg_user = User.objects.get(id=request.session['user_id'])
    non_missed_appointment = Appointment.objects.exclude(status="Missed")
    missed_appointments = Appointment.objects.filter(status="Missed")

    context = {
        "active_user": reg_user,
        "non_missed_appointments": non_missed_appointment,
        "missed_appointments": missed_appointments,
    }

    return render(request, 'home.html', context)