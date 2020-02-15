from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


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

class Calc(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=200, blank=True)
    areaResParameters = models.ForeignKey(AreaResParameters, on_delete=models.CASCADE)
    areaCalcParameters = models.ForeignKey(AreaCalcParameters, on_delete=models.CASCADE)
    srcParameters = models.ForeignKey(SrcParameters, on_delete=models.CASCADE)
