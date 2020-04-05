import sys
import os
import json

from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User



class Functional:
	verboseName = ''
	organ = ''
	typeDose = ''
	pathWay = ''
	age = ''
	comintment = True
	timeEnd = -1.
