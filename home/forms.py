from typing import Any, Dict
from django import forms

class demo_form(forms.Form):
    name = forms.CharField(label="User Name")
    email = forms.EmailField(label="User Email")
    age = forms.IntegerField(label="User Age")
    weight = forms.FloatField(label="User Weight")
    file = forms.FileField(label="File")
    # validation
    def clean(self) -> Dict[str, Any]:
        cleaned_data = super().clean()
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        if len(name) < 10:
            raise forms.ValidationError("sda")
        return cleaned_data