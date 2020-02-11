from django import forms

from .models import Calc

class CalcForm(forms.ModelForm):

    class Meta:
        model = Calc
        fields = (
            'name',
            'pathToCalc',
            "pathToADM",
            'comment',)
        labels = {
            'name' : 'Name of calculation',
            'pathToCalc' : 'Path to working folder',
            'pathToADM' : 'Path to Atmospheric Dispersion Model',
            'comment' : 'Comment of calculation'
        }
