from django import forms
from .models import Subscription


class SubCreateForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
