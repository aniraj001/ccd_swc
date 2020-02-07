from django import forms
from .models import Company, Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('company','hostel', 'room_no')
