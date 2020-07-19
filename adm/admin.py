from django.contrib import admin

from .models import Calc, AreaCalcParameters, AreaResParameters

admin.site.register(Calc)
admin.site.register(AreaCalcParameters)
admin.site.register(AreaResParameters)
