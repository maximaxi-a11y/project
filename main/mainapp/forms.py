from django import forms


class RegisterForm(forms.Form):
    your_mail = forms.CharField(label='your_mail', max_length=25)
    your_password = forms.CharField(label='your_password',max_length=20)
