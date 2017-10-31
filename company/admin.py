#coding: utf-8

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Company, School, Branch, ExamDetailItem, ExamItem, ExamType, ClassType

class CompanyInline(admin.StackedInline):
    model = Company
    extra = 1
    verbose_name = '分公司'
    verbose_name_plural = '分公司信息'

class BranchInline(admin.StackedInline):
    model = Branch
    extra = 1
    verbose_name = '分部'
    verbose_name_plural = '分部信息'

class SchoolAdmin(admin.ModelAdmin):
    inlines = (CompanyInline,)
    list_display = ('school_name', 'school_master')

class CompanyAdmin(admin.ModelAdmin):
    inlines = (BranchInline,)
    list_display= ('company_name', 'company_code', 'user')

class BranchAdmin(admin.ModelAdmin):
    list_display= ('branch_name', 'branch_code', 'company')

class ExamDetailItemInline(admin.StackedInline):
    model = ExamDetailItem
    extra = 1
    verbose_name = '考试明细项目'
    verbose_name_plural = '考试明细项目'

class ExamItemAdmin(admin.ModelAdmin):
    inlines = (ExamDetailItemInline,)
    list_display = ('item_name',)

class ExamDetailItemAdmin(admin.ModelAdmin):
    list_display = ('detail_name', 'get_item_name')
    def get_item_name(self, instance):
        return instance.item.item_name
    get_item_name.short_description = '所属项目'

class ClassTypeAdmin(admin.ModelAdmin):
    list_display = ('class_name',)

class ExamTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)

admin.site.register(ExamItem, ExamItemAdmin)
admin.site.register(ClassType, ClassTypeAdmin)
admin.site.register(ExamType, ExamTypeAdmin)
admin.site.register(ExamDetailItem, ExamDetailItemAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)

admin.AdminSite.site_header = 'Django Test'