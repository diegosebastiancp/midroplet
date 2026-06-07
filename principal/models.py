from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

# Create your models here.
class ubicacion(models.Model):
    id_ubi = models.AutoField(primary_key=True)
    latitud = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    longitud = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.latitud}, {self.longitud}"