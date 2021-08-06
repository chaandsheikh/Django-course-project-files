from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(required=False,
                             help_text='A valid email address, please.')
    password1 = forms.CharField(label='Enter password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        User.username = forms.CharField(max_length=100, required=False)
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password1']
        help_texts = {
            'username': None,
        }
