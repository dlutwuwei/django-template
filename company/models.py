# coding: utf-8

from django.db import models

from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

class School(models.Model):
    school_name = models.CharField('分校名称', max_length=200, unique=True)
    school_master = models.CharField('分校负责人', max_length=200, null=True, blank=True)
    def __str__(self):
      return self.school_name
    class Meta:
      verbose_name = '分校设置'
      verbose_name_plural = "分校设置"

class Company(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        verbose_name="所属分校",
        unique=False
    )
    user = models.ForeignKey(
      User,
      verbose_name="填报人",
      on_delete=models.CASCADE
    )
    company_name = models.CharField('分公司名称', max_length=200, unique=True)
    company_code = models.CharField('分公司代码', max_length=6, unique=True)
    def __str__(self):
      return self.company_name
    class Meta:
      verbose_name = '分公司设置'
      verbose_name_plural = '分公司设置'

class Branch(models.Model):
    company = models.ForeignKey(
      Company,
      verbose_name='所属公司',
      on_delete=models.CASCADE
    )
    branch_name = models.CharField('分部名称', max_length=200, unique=True)
    branch_code = models.CharField('分部代码', max_length=6, unique=True)
    class Meta:
      verbose_name = '分部设置'
      verbose_name_plural = '分部设置'
    def __str__(self):
      return self.branch_name


class ExamItem(models.Model):
    item_name = models.CharField('考试项目', max_length=100, unique=True)
    class Meta:
      verbose_name='考试项目'
      verbose_name_plural = '考试项目设置'
    def __str__(self):
      return self.item_name

class ExamDetailItem(models.Model):
    item = models.ForeignKey(
      ExamItem,
      on_delete=models.CASCADE,
      verbose_name="所属项目",
    )
    detail_name = models.CharField('考试明细项目', max_length=100, unique=True)
    class Meta:
      verbose_name='考试明细项目'
      verbose_name_plural = '考试明细项目设置'
    def __str__(self):
      return self.detail_name

class ExamType(models.Model):
    type_name = models.CharField('考试类型', max_length=100, unique=True)
    class Meta:
      verbose_name='考试类型'
      verbose_name_plural = '考试类型设置'
    def __str__(self):
      return self.type_name

class ClassType(models.Model):
    class_name = models.CharField('班型', max_length=100, unique=True)
    class Meta:
      verbose_name='班型'
      verbose_name_plural = '班型设置'
    def __str__(self):
      return self.class_name

class ProductType(models.Model):
    product_name = models.CharField('产品类型', max_length=100, unique=True)
    class Meta:
      verbose_name='产品类型'
      verbose_name_plural='产品类型设置'
    def __str__(self):
      return self.product_name

class IncomeConversion(models.Model):
    year = models.IntegerField('年份', default=2018)
    company = models.ForeignKey(Company, verbose_name="分公司")
    ratio = models.FloatField('收入转化率(%)')
    examItem = models.ForeignKey(ExamItem, verbose_name='考试项目')
    examDetailItem = ChainedForeignKey(
      ExamDetailItem,
      chained_field='examItem',
      chained_model_field="item",
      show_all=False,
      auto_choose=True,
      sort=True,
      on_delete=models.CASCADE,
      verbose_name="所属项目",
    )
    examType = models.ForeignKey(ExamType, verbose_name = '考试类型',max_length = 20, default=1)
    classType = models.ForeignKey(ClassType, verbose_name = '班型', max_length = 20, default=1)
    class Meta:
      verbose_name='收入转化率'
      verbose_name_plural='收入转化率设置'
    def __str__(self):
      return str(self.ratio)
