from django import forms

class chooseNumberForm(forms.Form):
    number = forms.IntegerField(label='Podaj numer')
