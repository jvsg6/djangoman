from django import forms

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
            'lat' : 'Lattitude of source',
            'lon' : 'Longitude of source',}
        # widgets = {
        #     'lon': Textarea(attrs={'cols': 80, 'rows': 20}),
        # }

class AreaCalcParametersForm(forms.ModelForm):
    class Meta:
        model = AreaCalcParameters
        fields = [
            'latMin',
            'lonMin',
            'latMax',
            'lonMax',]

        labels = {
            'latMin' : 'Min lattitude of calculation area',
            'lonMin' : 'Min longitude of calculation area',
            'latMax' : 'Max lattitude of calculation area',
            'lonMax' : 'Max longitude of calculation area',}

class AreaResParametersForm(forms.ModelForm):
    class Meta:
        model = AreaResParameters
        fields = [
            'latMin',
            'lonMin',
            'latMax',
            'lonMax',
            'countLon',
            'countLat',]

        labels = {
            'latMin' : 'Min lattitude of result area',
            'lonMin' : 'Min longitude of result area',
            'latMax' : 'Max lattitude of result area',
            'lonMax' : 'Max longitude of result area',
            'countLat' : 'Count cells in lattitude',
            'countLon' : 'Count cells in longitude',}


class WindarametersInAltForm(forms.ModelForm):
    class Meta():
        model = WindarametersInAlt
        fields = [
            'height',
            'direction',
            'speed',]
        labels = {
            'height' : 'Height of the wind',
            'direction' : 'Dierction of the wind',
            'Speed' : 'Speed of the wind',
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
            'meteoPhaseStart' : 'Meteo phase start time, s',
            'windConst' : 'Is wind constant in all height?',
            'precipitationsRate' : 'Rate of precipitation, mm/h',
            'precipitationType' : 'Type of precipitation',
            'stab' : 'Stability class',
            'roughness' : 'Roughness',
            'windLevels' : 'Wind on the varoius heights',
        }


class CalcForm(forms.ModelForm):
    class Meta():
        model = Calc
        fields = [
            'name',
            'comment',
            'windPhaseList',]
        labels = {
            'name' : 'Name of calculation',
            'comment' : 'Comment of calculation',
            'windPhaseList' : 'Input meteo phases',
        }
