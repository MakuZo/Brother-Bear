from django import forms

class ShortenURLForm(forms.Form):
    url = forms.URLField(label="URL to shorten")