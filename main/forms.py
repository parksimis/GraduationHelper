from django import forms

class LoginForm(forms.Form):
    user_id = forms.CharField(label='아이디', widget=forms.TextInput(attrs={
        'pattern': '[0-9]+',
        'title': '학번 입력',
    }))
    user_pwd = forms.CharField(label='비밀번호', widget=forms.PasswordInput())
