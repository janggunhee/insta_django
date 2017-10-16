from django import forms


class UserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput
    )
    password = forms.CharField(
        widget=forms.TextInput
    )
