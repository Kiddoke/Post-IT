from django.urls import path
from . import views

urlpatterns = [
    path('', views.tavle, name = 'tavle'),
    path('oppdater/<int:id>/', views.oppdater_status, name = 'oppdater_status'),
    path('slett/<int:id>/', views.slett, name = 'slett'),
]