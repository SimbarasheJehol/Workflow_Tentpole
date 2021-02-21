from django import forms
from frontendworkflow.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        extra_kwargs = {
            'types': {
                'allow_empty': False
            }
        }


