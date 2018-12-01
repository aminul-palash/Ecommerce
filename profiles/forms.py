from django import forms
from profiles.models import Profile
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ('first_name','last_name','bio','picture',)