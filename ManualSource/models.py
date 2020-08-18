from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.gis.db import models
# Create your models here.

class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.PolygonField()

class SrcParameters(models.Model):
    lat = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lon = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)
    poly = models.PolygonField(default='POLYGON((0.0 0.0, 0.0 50.0, 50.0 50.0, 50.0 0.0, 0.0 0.0))')

    def getPosition(self):
        return {"lat":self.lat, "lon":self.lon}