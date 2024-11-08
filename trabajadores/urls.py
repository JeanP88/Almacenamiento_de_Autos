from django.urls import path
from . views import trabajadores

urlpatterns = [
    path('', trabajadores, name='trabajadores'),
]