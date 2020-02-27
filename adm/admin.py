from django.contrib import admin

from .models import Calc, SrcParameters, AreaCalcParameters, AreaResParameters, CommonWindParameters, WindarametersInAlt

admin.site.register(Calc)
admin.site.register(SrcParameters)
admin.site.register(AreaCalcParameters)
admin.site.register(AreaResParameters)
admin.site.register(CommonWindParameters)
admin.site.register(WindarametersInAlt)
