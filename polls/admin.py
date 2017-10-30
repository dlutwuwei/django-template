#coding:utf-8
import unicodecsv as csv
from django.contrib import admin
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry
from django import forms
from itertools import chain

from company.models import Employee, Company

from .models import Question, Choice, Profit, Revenue, Collection, EnlistForcast, CostAdjust

from django.utils.dates import MONTHS
month_items = MONTHS.items()

def download_csv(modeladmin, request, queryset):
    if not request.user.is_staff:
        raise PermissionDenied
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response

download_csv.short_description = '导出excel数据'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = (
        ('question_text'),
        # for related fields
        #('id', RelatedDropdownFilter)
    )
    search_fields = ['question_text']
    actions = [download_csv]

class ChoiceAdmin(admin.ModelAdmin):
    fields = ('choice_text', 'votes')
    list_display = ('choice_text', 'votes')
    actions = [download_csv]

class ProfitAdmin(admin.ModelAdmin):
    fieldsets = [
        ('主营业务收入', {'fields': ['gongwuyuan', 'shiyedanwei', 'teacher']}),
        ('主营业务成本', {'fields': ['changdifei1', 'changdifei2', 'changdifei3']}),
        (None, {'fields': ['month']}),
        (None, {'fields': ['province']})
    ]
    list_display = ('month', 'province', 'gongwuyuan', 'shiyedanwei', 'teacher', 'changdifei1', 'changdifei2', 'changdifei3')
    list_filter = (
        ('month'),
        # for related fields
        #('id', RelatedDropdownFilter)
    )
    actions = [download_csv]
    def get_queryset(self, request):
        qs = super(ProfitAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # 此处user为当前model的related object的related object， 正常的外键只要filter(user=request.user)
        return qs.filter(province=request.user)

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name = 'user'
    verbose_name_plural = '公司信息'

class EnlistForm(forms.ModelForm):
    pass
    # company为外键，是多对一的关系, 隐藏字段，不可修改
    # company = forms.ModelChoiceField(
    #     queryset = Company.objects.all(),
    #     widget = forms.HiddenInput(),
    # )

class EnlistForcastAdmin(admin.ModelAdmin):
    form = EnlistForm
    actions = [download_csv]
    readonly_fields=('year',)
    list_filter =('company','company__school', 'year')
    list_display = ('company', 'examItem', 'examDetailItem', 'examType', 'classType',
        'examTime', 'studentConsumption', 'studentCount', 'get_revenue')
    def get_changeform_initial_data(self, request):
        companies = Company.objects.filter(user__id=request.user.id)
        if(companies):
            return {'company': companies[0].id}
    # 修改筛选后的列表
    def get_search_results(self, request, queryset, search_term):
        qs, x = super(EnlistForcastAdmin, self).get_search_results(request, queryset, search_term)
        if request.user.is_superuser:
            return qs, x
        else:
            companies = Company.objects.filter(user=request.user)
            print qs
            q = qs.filter(company__id = companies[0].id)
            print q, 'xxxx'
            for index, co in enumerate(companies):
                if(index == 0):
                    continue
                q = q | qs.filter(company__id = co.id)
            return q, x
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        print db_field.name
        if db_field.name == 'company':
            kwargs['queryset'] = Company.objects.filter(user=request.user)
        return super(EnlistForcastAdmin, self).formfield_for_foreignkey(db_field, request=None, **kwargs)
    # def get_month(self, instance):
    #     return month_items[int(instance.month)-1][1]
    # get_month.short_description = '月份'
    def get_revenue(self, instance):
        return instance.studentConsumption * instance.studentCount
    get_revenue.short_description = '预计学费收入(元)'

admin.site.register(Profit, ProfitAdmin)
admin.site.register(Collection)
admin.site.register(EnlistForcast, EnlistForcastAdmin)
admin.site.register(CostAdjust)
admin.site.register(Question, QuestionAdmin)
admin.site.register(LogEntry)
