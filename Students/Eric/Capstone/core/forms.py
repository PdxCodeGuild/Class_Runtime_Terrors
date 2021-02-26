  
from django import forms

from .models import Book, Ask


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('number', 'title', 'date', 'pdf' )

class AskForm(forms.ModelForm):
    class Meta:
        model = Ask
        fields = ('name', 'request', 'date' )