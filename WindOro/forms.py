from django import forms
from .models import WindOroPametersInAlt, CommonWindParameters
from .choices import *
from django.utils.translation import ugettext_lazy as _

class WindOroPametersInAltForm(forms.ModelForm):
    class Meta():
        model = WindOroPametersInAlt
        fields = [
            'height',
            'direction',
            'speed',]
        labels = {
            'height' : _('Height of the wind'),
            'direction' : _('Dierction of the wind'),
            'Speed' : _('Speed of the wind'),
        }

class CommonWindParametersForm(forms.ModelForm):
    class Meta():
        model = CommonWindParameters
        fields = [
            'meteoPhaseStart',
            'windConst',
            'precipitationsRate',
            'precipitationType',
            'stab',
            'roughness',
            'windLevels',]
        labels = {
            'meteoPhaseStart' : _('Meteo phase start time, s'),
            'windConst' : _('Is wind constant in all height?'),
            'precipitationsRate' : _('Rate of precipitation, mm/h'),
            'precipitationType' : _('Type of precipitation'),
            'stab' : _('Stability class'),
            'roughness' : _('Roughness'),
            'windLevels' : _('Wind on the varoius heights'),
        }
        #widgets = {'windLevels': forms.widgets.CheckboxSelectMultiple() }
