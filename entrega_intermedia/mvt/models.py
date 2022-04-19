from django.db import models

class Vuelo(models.Model):
    airline = models.CharField(max_length=40)
    number = models.IntegerField()

class Pasajero(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()

class Tripulacion(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    worked = models.CharField(max_length=40)
    
