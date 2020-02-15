from django import forms
from .models import Company, Room
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_no',)

    widgets = {
            'room_no': forms.Textarea(attrs={'class': 'form-control editable medium-editor-textarea postcontent'}),
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

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
