from django import forms


class ShortenURLForm(forms.Form):
    url = forms.URLField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "siimple-input siimple-input--fluid",
                "placeholder": "https://google.com",
            }
        ),
    )
