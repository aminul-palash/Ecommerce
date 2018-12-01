from django import forms
from bookmanagement.models import BookTransactionModel
from django.contrib.auth import get_user_model
User = get_user_model()

class BillingForm(forms.ModelForm):
  message = forms.CharField(label='', 
                widget=forms.Textarea(
                        attrs={'placeholder': "Your message...", 
                            "class": "form-control",
                            "resize": "none",
                            "cols": "6",
                            "rows": "4"}
                ))

  class Meta:
    model = BookTransactionModel
    fields = ['address','phone_number','message']
