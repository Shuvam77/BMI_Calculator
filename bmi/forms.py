from xml.parsers.expat import model
from django import forms

class BmiForm(forms.ModelForm):
    weightMetric = forms.FloatField()
    heightMetric = forms.FloatField()
    weightImperial = forms.FloatField()    
    feet = forms.FloatField()
    inches = forms.FloatField()
