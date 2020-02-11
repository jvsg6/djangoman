from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
class Calc(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pathToCalc = models.CharField(max_length=200)
    pathToADM = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=200, blank=True)




    def __str__(self):
        return self.pathToCalc
