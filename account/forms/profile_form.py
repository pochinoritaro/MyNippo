from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Eメール")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), min_length=8)