from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Post(models.Model):
    value = models.IntegerField(default=0,
                                validators=[
                                            MaxValueValidator(100),
                                            MinValueValidator(0)
                                           ]
                              ,)
    def __str__():
        return str(value)
