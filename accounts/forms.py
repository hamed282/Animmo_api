from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, OtpCode

from .models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number']


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password using <a href=\"../password/\" >'
                                                   'this form <a/>.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'is_active', 'is_admin', 'is_superuser']


class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)


class RegisterVerifyCodeForm(forms.Form):
    code = forms.IntegerField()


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=20)

