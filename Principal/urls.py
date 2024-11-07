from django.urls import path
from . import views

urlpatterns = [
    path('pedo', views.home, name='home'),
]