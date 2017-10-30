# coding: utf-8
from django import forms

from .models import Employee, Company



class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(
      label='分公司',
      max_length = 200,
    )

class myForm(forms.Form):
  province = forms.ChoiceField(
    widget = forms.Select(
      attrs={
        'class':'select',
        'onChange':'getCityOptions(this.value)'
        }),
      choices = PROVINCE_CHOICES,
      label= u'选择省'
    )

    city = forms.ChoiceField(
      widget = forms.Select(
        attrs={
          'class':'select',
          'onChange':'getDistrictOptions(this.value)',
          'style':'display:none'
      }),
      label = u'选择市'
    )