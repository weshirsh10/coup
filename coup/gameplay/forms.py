from django import forms

class PlayerForm(forms.Form):
    name = forms.CharField(label='Enter Your Name', max_length=20)