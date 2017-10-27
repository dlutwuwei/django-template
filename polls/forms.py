# coding: utf-8
from django import forms

from .models import Employee

PROVINCE_CHOICES = [
    ('henan', '河南'),
    ('beijing', '北京'),
    ('shanghai', '上海'),
    ('henan', '河南'),
    ('beijing', '北京'),
    ('shanghai', '上海'),
]

class EmployeeForm(forms.ModelForm):
    department = forms.CharField(
      label='部门',
      max_length = 10,
      widget = forms.Select(choices=PROVINCE_CHOICES)
    )
