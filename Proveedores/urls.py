from django.urls import path
from . views import proveedores

urlpatterns = [
    path('', proveedores, name='proveedores'),
]