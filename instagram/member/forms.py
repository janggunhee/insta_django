from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    # clean_<field_name>
    def clean_username(self):
        data =self.cleaned_data['username']
        # 유저가 존재하면 forms.ValidationError를 발생
        # 아니면 data return

        if User.objects.filter(username=data).exist():
            raise forms.ValidationError("사용자가 이미 존재 합니다.")

        return data

