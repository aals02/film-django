Here's the code with proper indentations:

```python
from django import forms
from .models import User
from formValidationApp.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'username', 'password', 'repeat_password', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        repeat_password = self.cleaned_data.get('repeat_password')
        username = self.cleaned_data.get('username')

        if password != repeat_password:
            raise forms.ValidationError("The passwords do not match.")

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
