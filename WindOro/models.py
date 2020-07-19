from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import *
# Create your models here.

class WindOroPametersInAlt(models.Model):
    height = models.FloatField(validators=[MinValueValidator(0.)], null=True, blank=True)
    direction = models.FloatField(validators=[MinValueValidator(0.)], null=True, blank=True)
    speed = models.FloatField(validators=[MinValueValidator(0.)], null=True, blank=True)

class CommonWindParameters(models.Model):
    meteoType = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    meteoPhaseStart = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    windConst = models.IntegerField(choices=WIND_CONST_CHOICES, default=0, null=True, blank=True)
    precipitationsRate = models.FloatField(validators=[MinValueValidator(0.)], null=True, blank=True)
    precipitationType = models.FloatField(choices=PRECIPITATION_TYPE, default=0, null=True, blank=True)
    stab = models.CharField(max_length=1, choices=STABILITY_CLASS, default="D", null=True, blank=True)
    roughness = models.FloatField(validators=[MinValueValidator(0.)], null=True, blank=True)
    windLevels = models.ManyToManyField(WindOroPametersInAlt, symmetrical=False, blank=True)