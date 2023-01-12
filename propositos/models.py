from datetime import datetime, date, timedelta

from django.db import models
from django.utils import timezone
# from django.contrib import admin

class Proposito(models.Model):
     proposito = models.CharField(max_length=255)
     fechaObjetivo = models.DateField()
     conseguido = models.BooleanField(null=True)
     fechaConseguido = models.DateField(null=True)
     
     @property
     def propositoProximo(self):
          # Devuelve si el proposito se tiene que cumplir en menos de 30 dias
          fechaActual = date.today()
          return fechaActual <= self.fechaObjetivo <= fechaActual + timedelta(days = 30)
     
     @property
     def propositoCaducado(self):
          # Devuelve si el proposito ha caducado ya
          fechaActual = date.today()
          return fechaActual > self.fechaObjetivo