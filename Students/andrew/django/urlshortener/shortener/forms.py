from django import forms


class Url(forms.Form):
    url = forms.CharField(label="Enter a URL to shorten.")