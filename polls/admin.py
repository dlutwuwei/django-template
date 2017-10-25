#coding:utf-8
import unicodecsv as csv
from django.contrib import admin
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

from .models import Question, Choice, Profit, RevenueForcast, Collection, EnlistForcast, CostForcast, CostAdjust, OperatingCost

from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

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
        ('question_text', DropdownFilter),
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
        ('month', DropdownFilter),
        # for related fields
        #('id', RelatedDropdownFilter)
    )
    actions = [download_csv]


admin.site.register(Profit, ProfitAdmin)
admin.site.register(RevenueForcast)
admin.site.register(Collection)
admin.site.register(EnlistForcast)
admin.site.register(CostForcast)
admin.site.register(CostAdjust)
admin.site.register(OperatingCost)

admin.AdminSite.site_header = '华图教育2018预算'