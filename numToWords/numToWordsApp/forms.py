from django import forms

class ChooseNumberForm(forms.Form):
    number = forms.IntegerField(label='Podaj numer')
