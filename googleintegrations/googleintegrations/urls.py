from django.contrib import admin
from django.urls import path, include
from calenders.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('rest/v1/calendar/', include('calenders.urls')),
]
