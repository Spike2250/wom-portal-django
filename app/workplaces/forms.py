from django import forms
from .models import Workplace


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = [
            'name',
        ]
