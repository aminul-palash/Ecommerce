from django import forms
from .models import Comments
from django.contrib.auth import get_user_model
User = get_user_model()
class CommentsForm(forms.ModelForm):
  comment = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Your comments...", 
                            "class": "form-control",
                            "cols": "6",
                            "rows": "4"}
                ))
  class Meta: 
    model = Comments
    fields = ['comment']
   
