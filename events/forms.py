from django import forms
from .models import Event
from datetime import datetime

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        now = datetime.now().strftime('%Y-%m-%dT%H:%M')  # format for datetime-local
        self.fields['date'].widget = forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control',
            'min': now,
        })
