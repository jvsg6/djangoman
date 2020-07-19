from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from ManualSource.models import SrcParameters
from WindOro.models import CommonWindParameters, WindOroPametersInAlt

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
