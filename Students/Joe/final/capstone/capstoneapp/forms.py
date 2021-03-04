from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(label = 'title', max_length=200)
    class Meta:
        model = Post
        fields = ('title', 'text')