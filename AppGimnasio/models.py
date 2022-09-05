from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField(unique=True, max_length=8)

class Actividad(models.Model):
    nombre = models.CharField(max_length=40)
    profesor = models.CharField(max_length=40)

class Cuota(models.Model):
    pago = models.BooleanField()
    fecha_de_pago = models.DateField()
