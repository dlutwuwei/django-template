#coding:utf-8
import unicodecsv as csv
from django.contrib import admin
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Question, Choice, Profit, RevenueForcast, Collection, EnlistForcast, CostForcast, CostAdjust, OperatingCost, Employee
from .forms import EmployeeForm

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

class EmployeeInline(admin.TabularInline):
    model = Employee
    form  = EmployeeForm
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

admin.site.register(Profit, ProfitAdmin)
admin.site.register(RevenueForcast)
admin.site.register(Collection)
admin.site.register(EnlistForcast)
admin.site.register(CostForcast)
admin.site.register(CostAdjust)
admin.site.register(OperatingCost)
admin.site.register(Question, QuestionAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.AdminSite.site_header = '华图教育2018预算'