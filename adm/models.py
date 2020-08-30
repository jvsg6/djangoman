import random

from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from ManualSource.models import SrcParameters
from WindOro.models import CommonWindParameters, WindOroPametersInAlt
from django.contrib.gis.db import models

class AreaCalcParameters(models.Model):
    latMinCalc = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMinCalc = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    latMaxCalc = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMaxCalc = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    areaCalc = models.PolygonField(default='POLYGON((0.0 0.0, 0.0 50.0, 50.0 50.0, 50.0 0.0, 0.0 0.0))')


class AreaResParameters(models.Model):
    latMinRes = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMinRes = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    latMaxRes = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lonMaxRes = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    areaRes = models.PolygonField(default='POLYGON((0.0 0.0, 0.0 50.0, 50.0 50.0, 50.0 0.0, 0.0 0.0))')

    countLonRes = models.IntegerField(null=True, blank=True)
    countLatRes = models.IntegerField(null=True, blank=True)


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
    
    transportStatus = models.IntegerField(blank=True, null=True, default=0)
    weatherStatus = models.IntegerField(blank=True, null=True, default=0)
    
    def setRandParameters(self):
        countCalcs = Calc.objects.count()
        self.name = "Calculation " + str(countCalcs+1)
        latInit = -88.0 + random.random()*176.0
        lonInit = -178.0 + random.random()*356.0
        lonMin = lonInit-0.5
        lonMax = lonInit+0.5
        latMin = latInit-0.5
        latMax = latInit+0.5
        self.areaResParam.lonMinRes = lonMin
        self.areaResParam.latMinRes = latMin
        self.areaResParam.lonMaxRes = lonMax
        self.areaResParam.latMaxRes = latMax
        self.areaResParam.countLonRes = 51
        self.areaResParam.countLatRes = 51
        self.areaCalcParam.lonMinCalc = lonMin
        self.areaCalcParam.latMinCalc = latMin
        self.areaCalcParam.lonMaxCalc = lonMax
        self.areaCalcParam.latMaxCalc = latMax
        self.srcParam.lon = lonInit
        self.srcParam.lat = latInit
