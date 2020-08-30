from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class SrcParameters(models.Model):
    lat = models.FloatField(validators=[MinValueValidator(-90.), MaxValueValidator(90.)], null=True, blank=True)
    lon = models.FloatField(validators=[MinValueValidator(-180.), MaxValueValidator(180.)], null=True, blank=True)

    def getPosition(self):
        return {"lat":self.lat, "lon":self.lon}