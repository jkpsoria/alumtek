from socket import fromshare
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class PasswordChangingForm(PasswordChangeForm):

    old_password = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Old password'}))
    new_password1 = forms.CharField(label="New Password",  widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'New password'}))
    new_password2 = forms.CharField(label = "Password Confirmation",  widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password', 'placeholder':'Confirm new password'}))

    class Meta:
        model = User
        fields = ('old_password' , 'new_password1', 'new_password2')
