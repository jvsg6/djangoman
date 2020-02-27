from django import forms

from .models import Calc, SrcParameters, AreaCalcParameters, AreaResParameters, WindarametersInAlt


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


class CalcForm(forms.ModelForm):
    class Meta():
        model = Calc
        fields = [
            'name',
            'comment',
            'windLevels',]
        labels = {
            'name' : 'Name of calculation',
            'comment' : 'Comment of calculation',
            'windLevels' : 'Input wind levels'
        }
