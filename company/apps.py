#coding: utf-8

from django.apps import AppConfig
import sys
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class CompanyConfig(AppConfig):
    name = 'company'
    verbose_name = '公司设置'
