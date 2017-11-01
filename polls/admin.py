#coding:utf-8
import unicodecsv as csv
from django.contrib import admin
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.admin.models import LogEntry
from django import forms

from company.models import Company, IncomeConversion
from guardian.shortcuts import assign_perm
from django.utils.dates import MONTHS
from .models import Profit, Revenue, EnlistForcast, CostAdjust

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

class BaseAdmin(admin.ModelAdmin):
    # 保存实例数据库时加上权限
    def save_model(self, request, obj, form, change):
        # 对象实例需要先存储，再加权限
        super(BaseAdmin, self).save_model(request, obj, form, change)
        perm = obj._meta.permissions[0][0]
        assign_perm(perm, request.user, obj)
    # 过滤筛选后的列表
    def get_search_results(self, request, queryset, search_term):
        qs, use_restrict = super(BaseAdmin, self).get_search_results(request, queryset, search_term)
        ids = []
        # 管理员默认拥有所有权限
        for obj in qs:
            perm = obj._meta.permissions[0][0]
            # print perm, request.user.has_perm(perm, obj)
            if(request.user.has_perm(perm, obj)):
                ids.append(obj.id)
        return qs.filter(id__in=ids), use_restrict


@admin.register(Profit)
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

class EnlistForm(forms.ModelForm):
    conversion = forms.ModelChoiceField(
        queryset=IncomeConversion.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )

@admin.register(EnlistForcast)
class EnlistForcastAdmin(BaseAdmin):
    form = EnlistForm
    actions = [download_csv]
    readonly_fields=('year',)
    list_filter =('branch', 'company','company__school', 'year')
    list_display = (
        'company',
        'branch',
        'examItem',
        'examDetailItem',
        'examType',
        'classType',
        'productType',
        'examTime',
        'studentConsumption',
        'studentCount',
        'get_revenue',
        'get_conversion',
        'get_income'
    )
    # 初始化填表信息
    def get_changeform_initial_data(self, request):
        companies = Company.objects.filter(user__id=request.user.id).only('id')
        if(companies):
            return {'company': companies[0].id}
    # 过滤下拉条菜单
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'company':
            kwargs['queryset'] = Company.objects.filter(user=request.user)
        return super(EnlistForcastAdmin, self).formfield_for_foreignkey(db_field, request=None, **kwargs)
    def get_revenue(self, instance):
        return instance.studentConsumption * instance.studentCount
    get_revenue.short_description = '预计学费(元)'
    def get_conversion(self,instance):
        if instance.conversion:
            return str(instance.conversion) + '%'
        else:
            return '-'
    get_conversion.short_description = '转化率'
    def get_income(self, instance):
        if(instance.conversion):
            return self.get_revenue(instance) * float(instance.conversion.ratio) / 100
        else:
            return '0.0'
    get_income.short_description = '预计确认收入(元)'
    # 保存时，查找转化率
    def save_model(self, request, obj, form, change):
        # print '-------', obj.conversion, obj.examItem, obj.examDetailItem, obj.examType, obj.classType
        try:
            obj.conversion = IncomeConversion.objects.all().get(
                company= obj.company,
                examItem = obj.examItem,
                examDetailItem = obj.examDetailItem,
                examType = obj.examType,
                classType = obj.classType,
            )
        except Exception:
            pass

        # print '=======', obj.conversion
        # 对象实例需要先存储，再加权限
        super(EnlistForcastAdmin, self).save_model(request, obj, form, change)



admin.site.register(CostAdjust)
admin.site.register(LogEntry)
