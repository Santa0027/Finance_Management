from django import forms
from .models import Company, Individual

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'phone', 'industry', 'logo', 'address']

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['name', 'email', 'phone']
