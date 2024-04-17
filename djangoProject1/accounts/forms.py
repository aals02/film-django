from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        if not User.objects.filter(email=email, username=username).exists():
            raise ValidationError("No matching user found.")
        return cleaned_data
