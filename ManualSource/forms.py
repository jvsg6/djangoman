from django import forms
from .models import SrcParameters
from django.utils.translation import ugettext_lazy as _


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