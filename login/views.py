from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strftime
#import bcrypt

from .models import User
from home.models import Appointment

# Create your views here.
def login(request):
    return render(request, 'index.html')

def registrar(request):
    return render(request, 'index.html')

def inicio(request):
    usuario = User.objects.filter(email=request.POST['email'])
    errores = User.objects.validar_login(request.POST, usuario)

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = usuario[0].id
        return redirect('home/')

def registro(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registrar')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        decode_hash_pw = password.decode('utf-8')
        #crear usuario
        if request.POST['rol'] == '1':
            user = User.objects.create(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=1,
            )
        else:
            user = User.objects.create(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                email=request.POST['email'],
                password=decode_hash_pw,
                rol=2,
            )
        request.session['user_id'] = user.id
    return redirect('home/')

def logout(request):
    request.session.flush()
    return redirect('/')

def create_appointment(request):
    return render(request, 'add_appointment.html')

def add_appointment(request):
    task = request.POST['task']
    date = request.POST['date']
    status = request.POST['status']
    user = User.objects.filter(id=request.session['user_id'])
    Appointment.objects.create(task=task, date=date, status=status, user=user[0])
    return redirect('home/')

def edit_appointment(request):
    return render(request, 'edit_appointment.html')
