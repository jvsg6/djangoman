from django.contrib import admin

from .models import Calc, SrcParameters, AreaCalcParameters, AreaResParameters

admin.site.register(Calc)
admin.site.register(SrcParameters)
admin.site.register(AreaCalcParameters)
admin.site.register(AreaResParameters)
