from django import forms
from .models import Club

class Play_Match(forms.Form):
    player_1 = forms.IntegerField(widget=forms.TextInput(attrs={'size':10, 'maxlength':2}))
    player_2 = forms.IntegerField(widget=forms.TextInput(attrs={'size':10, 'maxlength':2}))
    
