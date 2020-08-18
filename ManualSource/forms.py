from django import forms
from .models import SrcParameters, Zipcode
from django.utils.translation import ugettext_lazy as _

Zipcode


class ZipcodeForm(forms.ModelForm):
    class Meta:
        model = Zipcode
        fields = [
            'code',
            'poly',]

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