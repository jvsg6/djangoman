from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from .choices import *

class SrcParameters(models.Model):
    lat = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lon = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)

    def getPosition(self):
        return {"lat":self.lat, "lon":self.lon}

class AreaCalcParameters(models.Model):
    latMinCalc = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMinCalc = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    latMaxCalc = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMaxCalc = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)

class AreaResParameters(models.Model):
    latMinRes = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMinRes = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    latMaxRes = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMaxRes = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    countLonRes = models.IntegerField(null=True, blank=True)
    countLatRes = models.IntegerField(null=True, blank=True)

class WindarametersInAlt(models.Model):
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
    windLevels = models.ManyToManyField(WindarametersInAlt, symmetrical=False, blank=True)

class Calc(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    comment = models.CharField(max_length=200, null=True, blank=True)
    areaResParam = models.ForeignKey(AreaResParameters, on_delete=models.CASCADE, null=True, blank=True)
    areaCalcParam = models.ForeignKey(AreaCalcParameters, on_delete=models.CASCADE, null=True, blank=True)
    srcParam= models.ForeignKey(SrcParameters, on_delete=models.CASCADE, null=True, blank=True)
    calcADMReturn = models.IntegerField(blank=True, null=True)
    pathToInput = models.CharField(max_length=1000, null=True, blank=True)
    pathToLanduse = models.CharField(max_length=1000, null=True, blank=True)
    pathToOut = models.CharField(max_length=1000, null=True, blank=True)
    windPhaseList = models.ManyToManyField(CommonWindParameters, blank=True, symmetrical=False)

    calcAMDPopen = None
