# coding: utf-8
from django import forms

from .models import Employee, Company


# def get_object():
#     r = [('', '----')]
#     for obj in Company.objects.all():
#        r = r + [(obj, obj.company_name)]
#     return r

# class EmployeeForm(forms.ModelForm):
#     department = forms.CharField(
#       label='分公司',
#       max_length = 200,
#       widget = forms.Select(choices=get_object())
#     )
