#coding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Employee, Company, School
# from .forms import EmployeeForm


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name = 'user'
    verbose_name_plural = '公司信息'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)
    list_display = ('username', 'email', 'last_name', 'first_name', 'is_staff', 'get_department')
    def get_department(self, instance):
        return instance.employee.company
    get_department.short_description = '分公司'


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'school_master')

class CompanyAdmin(admin.ModelAdmin):
    list_display= ('company_name', 'company_code')


admin.site.register(School, SchoolAdmin)
admin.site.register(Company, CompanyAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.AdminSite.site_header = '华图教育2018预算'