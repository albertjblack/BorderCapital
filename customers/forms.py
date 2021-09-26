from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from . import models

class CustomerCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", 'email',"password1", "password2")
        model = models.Customer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email address"
        for field in self.fields:
            self.fields[field].help_text=''

    def clean_username(self):
        return self.cleaned_data['username'].lower()

class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ('first_name','last_name','username', 'email','profile_pic')
        