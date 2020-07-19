from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Calc, AreaCalcParameters, AreaResParameters
from django.forms import ModelForm, Textarea


class DownloadForm():
    # filesToDownload = forms.MultipleChoiceField(
    #     label='label',
    #     help_text='help',
    #     choices=['A', 'B', 'C'],
    #     widget=forms.CheckboxSelectMultiple,)

    isInputFileReq = forms.BooleanField()
    isLanduseFileReq = forms.BooleanField()
    isOutFileReq = forms.BooleanField()



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
