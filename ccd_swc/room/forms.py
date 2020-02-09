from django import forms
from .models import Company, Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('hostel', 'room_no')

    widgets = {
            'hostel': forms.TextInput(attrs={'class': 'textinputclass'}),
            'room_no': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class FilebabyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'industry', 'poc')

    widgets = {
            'name': forms.TextInput(attrs={'class': 'textinputclass'}),
            'industry': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'poc': forms.TextInput(attrs={'class': 'textinputclass'}),
        }
