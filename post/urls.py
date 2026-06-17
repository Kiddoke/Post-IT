from django.urls import path
from . import views

urlpattens = [ path('', views.postIT, name = 'tavle') ]