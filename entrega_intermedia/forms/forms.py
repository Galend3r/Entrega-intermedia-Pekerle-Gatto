from django import forms

class VueloForms(forms.Form):
    airline = forms.CharField(max_length=40)
    number = forms.IntegerField()

class PasajeroForms(forms.Form):
    name = forms.CharField(max_length=40)
    lastname = forms.CharField(max_length=40)
    email = forms.EmailField()

class TripulacionForms(forms.Form):
    name = forms.CharField(max_length=40)
    lastname = forms.CharField(max_length=40)
    worked = forms.CharField(max_length=40)
    