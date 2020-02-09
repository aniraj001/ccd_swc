from django import forms
from .models import Company, Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('hostel', 'room_no')

class FilebabyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'industry', 'poc','logo')
