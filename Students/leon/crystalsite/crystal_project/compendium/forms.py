from django import forms
from django.core.exceptions import ValidationError
from .models import Crystal, Tag

class SlugCleanMixin:
     def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if (new_slug == 'create'):
            raise ValidationError('Slug may not be "create".')
        return new_slug

class CrystalForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Crystal
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name']

class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()


