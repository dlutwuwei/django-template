# coding: utf-8
from django import forms

from .models import Employee, Company



class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(
      label='分公司',
      max_length = 200,
    )
