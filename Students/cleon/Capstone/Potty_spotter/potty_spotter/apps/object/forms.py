from django import forms
from potty_spotter.apps.object import models


class BaseForm(forms.ModelForm):
    required_css_class = 'required'


class RestroomCreateForm(BaseForm):
    class Meta:
        model = models.Restroom
        fields = (
            'name',
            'latitude',
            'longitude'
        )


class RestroomUpdateForm(BaseForm):
    class Meta:
        model = models.Restroom
        fields = (
            'name',
            'latitude',
            'longitude'
        )
