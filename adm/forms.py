from django import forms

from .models import Calc

class CalcForm(forms.ModelForm):

    class Meta:
        model = Calc
        fields = ('pathToCalc',)
