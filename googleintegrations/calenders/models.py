from django.db import models
from django.contrib.auth.models import User

class GoogleCalendar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=200)
    access_token = models.CharField(max_length=500)
    refresh_token = models.CharField(max_length=500)
