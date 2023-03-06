from django import forms
from .models import *


class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'content']