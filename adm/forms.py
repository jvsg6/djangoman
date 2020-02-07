from django import forms

from .models import Calc

class CalcForm(forms.ModelForm):

    class Meta:
        model = Calc
        fields = (
            'author',
            'pathToCalc',
            "pathToADM",)
        labels = {
            'author' : 'Calculation create by',
            'pathToCalc' : 'Path to working folder',
            'pathToADM' : 'Path to Atmospheric Dispersion Model',
        }
