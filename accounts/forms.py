from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ValidationError
from .models import CustomUser,Profile
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from allauth.account.adapter import DefaultAccountAdapter


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields =('first_name','last_name','email','mobile',)
   
    


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields =('first_name','last_name','email','mobile',)
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
class ProfileUpdate(forms.ModelForm) : 
    class Meta : 
        model = Profile
        fields = ("username","gender","date_of_birth","image")
    def __init__(self, *args, **kwargs):
        super(ProfileUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
