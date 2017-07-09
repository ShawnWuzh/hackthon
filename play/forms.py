from django import forms
from .models import Play

class PlayForm(forms.ModelForm):
    time = forms.DateTimeField()
    class Meta:
        model = Play
        exclude = ('timestamp','owner','num_of_participants','participants','slug',)

class PartipateForm(forms.Form):
    timestamp = forms.HiddenInput()