from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from .choices import *

class SrcParameters(models.Model):
    lat = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)])
    lon = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)])

    def getPosition(self):
        return {"lat":self.lat, "lon":self.lon}

class AreaCalcParameters(models.Model):
    latMin = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)])
    lonMin = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)])
    latMax = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)])
    lonMax = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)])

class AreaResParameters(models.Model):
    latMin = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)])
    lonMin = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)])
    latMax = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)])
    lonMax = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)])
    countLon = models.IntegerField()
    countLat = models.IntegerField()

class WindarametersInAlt(models.Model):
    height = models.FloatField(validators=[MinValueValidator(0.)])
    direction = models.FloatField(validators=[MinValueValidator(0.)])
    speed = models.FloatField(validators=[MinValueValidator(0.)])

class CommonWindParameters(models.Model):
    meteoType = models.IntegerField(validators=[MinValueValidator(0)])
    meteoPhaseStart = models.IntegerField(validators=[MinValueValidator(0)])
    windConst = models.IntegerField(choices=WIND_CONST_CHOICES, default=0)
    precipitationsRate = models.FloatField(validators=[MinValueValidator(0.)])
    precipitationType = models.FloatField(choices=PRECIPITATION_TYPE, default=0)
    stab = models.CharField(max_length=1, choices=STABILITY_CLASS, default="D")
    roughness = models.FloatField(validators=[MinValueValidator(0.)])
    windLevels = models.ManyToManyField(WindarametersInAlt, symmetrical=False)

class Calc(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=200, blank=True)
    areaResParameters = models.ForeignKey(AreaResParameters, on_delete=models.CASCADE)
    areaCalcParameters = models.ForeignKey(AreaCalcParameters, on_delete=models.CASCADE)
    srcParameters = models.ForeignKey(SrcParameters, on_delete=models.CASCADE)
    calcADMReturn = models.IntegerField(blank=True, null=True)
    pathToInput = models.CharField(max_length=1000, blank=True)
    pathToLanduse = models.CharField(max_length=1000, blank=True)
    pathToOut = models.CharField(max_length=1000, blank=True)
    windPhaseList = models.ManyToManyField(CommonWindParameters, blank=True, symmetrical=False)
    calcAMDPopen = None
