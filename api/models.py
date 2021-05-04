from django.db import models

class Cadena(models.Model):
    secuencia = models.TextField(blank=True)
