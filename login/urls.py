from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('registrar', views.registrar),
    path('inicio', views.inicio),
    path('registro', views.registro),
    path('logout', views.logout),
    path('create_appointment', views.create_appointment, name='create_appointment'),
    path('add_appointment', views.add_appointment, name='add_appointment'),
    path('edit_appointment', views.edit_appointment, name='edit_appointment'),
]