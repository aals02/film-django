from django import forms
from .models import User
from logging import PlaceHolder

class UserForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'name'
    # }))
    # dob = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'age'
    # }))
    # username = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'username'
    # }))
    # password = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'password'
    # }))
    # email = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'email'
    # }))
    # # needs to be drop down with images not text area
    # # pfp = forms.CharField(widget=forms.Textarea(attrs={
    # #     'class': 'form-control',
    # #     'placeholder': 'pfp'
    # # }))
    class Meta:
        model = User
        fields = ['name', 'dob', 'username', 'password', 'email']

    def clean(self):
        # cleaned_data = super().clean()
        super(UserForm, self).clean()
        
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
