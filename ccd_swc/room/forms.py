from django import forms
from .models import Company, Room
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_no',)

class FilebabyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'industry', 'poc')

    widgets = {
            'name': forms.TextInput(attrs={'class': ''}),
            'industry': forms.Textarea(attrs={'class': ''}),
            'poc': forms.TextInput(attrs={'class': ''}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
