from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

class Calc(models.Model):
    pathToCalc = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.pathToCalc
