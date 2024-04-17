from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from logging import PlaceHolder
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

User = get_user_model()
print(type(User))
class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'name'
    }))
    dob = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'age'
    }))
    username = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'username'
    }))
    password = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'password'
    }))
    email = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'email'
    }))
    #needs to be drop down with images not text area
    pfp = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'pfp'
    }))
    class Meta:
        model = User
        fields = ['name', 'dob', 'username', 'password', 'email']

    def clean(self):
        cleaned_data = super().clean()
        # super(UserForm, self).clean()

        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')

        # if password != repeat_password:
        #     raise forms.ValidationError("The passwords do not match.")

        if len(password) < 6:
            self._errors['password'] = self.error_class([
                'Minimum 8 characters required'])

        if len(password) > 100:
            self._errors['password'] = self.error_class([
                'Maximum 100 characters allowed'])

        if len(username) < 6:
            self._errors['username'] = self.error_class([
                'Minimum 6 characters required'])

        if len(username) > 100:
            self._errors['username'] = self.error_class([
                'Maximum 100 characters required'])

        return self.cleaned_data

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name = forms.CharField(max_length=254, help_text='Required. Inform a valid name')
    dob = forms.DateField(widget = forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'dob', 'name')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

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

