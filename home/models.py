from django.db import models
from login.models import User
# Create your models here.

class Appointment(models.Model):
    task = models.CharField(max_length=30)
    date = models.DateTimeField()
    status = models.CharField(max_length=7)
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)