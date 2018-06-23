from django import forms
from django.forms import fields

class UserSignInForm(forms.Form):
    username=fields.CharField(
        widget=forms.TextInput({
            'id':"inputEmail",
            'class':"form-control",
            'placeholder':"用户名",
            'name':"username",
        }),
        max_length=12,
    )
    passwd=fields.CharField(
        widget=forms.PasswordInput({
            'type':"password",
            'id':"inputPassword",
            'class':"form-control",
            'name':"password",
            'placeholder':"密码"
        }),
        max_length=12,
    )

class UserSignUpForm(forms.Form):
    username=fields.CharField(
        widget=forms.TextInput({
            'id':"inputEmail",
            'class':"form-control",
            'placeholder':"用户名",
            'name':"username",
        }),
        max_length=12,
    )
    passwd1=fields.CharField(
        widget=forms.PasswordInput({
            'type':"password",
            'id':"inputPassword1",
            'class':"form-control",
            'name':"password1",
            'placeholder':"密码"
        }),
        max_length=12,
    )
    passwd2=fields.CharField(
        widget=forms.PasswordInput({
            'type':"password",
            'id':"inputPassword2",
            'class':"form-control",
            'name':"password2",
            'placeholder':"确认密码"
        }),
        max_length=12,
    )