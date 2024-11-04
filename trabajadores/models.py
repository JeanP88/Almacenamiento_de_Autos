from django.db import models


class Trabajador(models.Model):
    name = models.CharField(max_length=150)
    lastName = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    typeWork = models.CharField(max_length=200)
    cedula = models.CharField(max_length=200)
    codigo_de_empleado = models.CharField(max_length=200)
    image = models.CharField(max_length=700)
