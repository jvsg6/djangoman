from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Calc, SrcParameters, AreaCalcParameters, AreaResParameters, WindarametersInAlt, CommonWindParameters
from django.forms import ModelForm, Textarea
from .choices import *
class DownloadForm():
    # filesToDownload = forms.MultipleChoiceField(
    #     label='label',
    #     help_text='help',
    #     choices=['A', 'B', 'C'],
    #     widget=forms.CheckboxSelectMultiple,)

    isInputFileReq = forms.BooleanField()
    isLanduseFileReq = forms.BooleanField()
    isOutFileReq = forms.BooleanField()



class SrcParametersForm(forms.ModelForm):
    class Meta:
        model = SrcParameters
        fields = [
            'lat',
            'lon',]

        labels = {
            'lat' : _('Latitude of source'),
            'lon' : _('Longitude of source'),}
        # widgets = {
        #     'lon': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

class AreaCalcParametersForm(forms.ModelForm):
    class Meta:
        model = AreaCalcParameters
        fields = [
            'latMinCalc',
            'lonMinCalc',
            'latMaxCalc',
            'lonMaxCalc',]

        labels = {
            'latMinCalc' : _('Min latitude of calculation area'),
            'lonMinCalc' : _('Min longitude of calculation area'),
            'latMaxCalc' : _('Max latitude of calculation area'),
            'lonMaxCalc' : _('Max longitude of calculation area'),}

class AreaResParametersForm(forms.ModelForm):
    class Meta:
        model = AreaResParameters
        fields = [
            'latMinRes',
            'lonMinRes',
            'latMaxRes',
            'lonMaxRes',
            'countLonRes',
            'countLatRes',]

        labels = {
            'latMinRes' : _('Min latitude of result area'),
            'lonMinRes' : _('Min longitude of result area'),
            'latMaxRes' : _('Max latitude of result area'),
            'lonMaxRes' : _('Max longitude of result area'),
            'countLatRes' : _('Count cells in latitude'),
            'countLonRes' : _('Count cells in longitude'),}


class WindOroPametersInAltForm(forms.ModelForm):
    class Meta():
        model = WindarametersInAlt
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


class CalcForm(forms.ModelForm):
    class Meta():
        model = Calc
        fields = [
            'name',
            'comment',
            'windPhaseList',]
        labels = {
            'name' : _('Name of calculation'),
            'comment' : _('Comment of calculation'),
            'windPhaseList' : _('Input meteo phases'),
        }
