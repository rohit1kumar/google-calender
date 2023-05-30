from django.contrib import admin

# Register session table which is used to store the credentials
from django.contrib.sessions.models import Session

admin.site.register(Session)