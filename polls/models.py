#coding: utf-8
import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
      return self.question_text
    def was_published_recently(self):
      now = timezone.now()
      return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    class Meta:
      verbose_name = "问题报表"
      verbose_name_plural = "问题报表"

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
      return self.choice_text
    class Meta:
      verbose_name = "选项"
      verbose_name_plural = "选项报表"

@python_2_unicode_compatible
class Profit(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    changdifei1 = models.FloatField('场地费1', default=0)
    changdifei2 = models.FloatField('场地费2', default=0)
    changdifei3 = models.FloatField('场地费3', default=0)
    province = models.CharField('省份', max_length=200)
    def __str__(self):
      return "profit"
    class Meta:
      verbose_name = "利润"
      verbose_name_plural = "利润报表"

class RevenueForcast(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "主营业务收入预测"
      verbose_name_plural = "主营业务收入预测报表"

class Collection(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "收款汇总"
      verbose_name_plural = "收款汇总报表"

class EnlistForcast(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "考情及报名收入预测"
      verbose_name_plural = "考情及报名收入预测报表"

class CostForcast(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    changdifei1 = models.FloatField('场地费1', default=0)
    changdifei2 = models.FloatField('场地费2', default=0)
    changdifei3 = models.FloatField('场地费3', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "主营业务成本"
      verbose_name_plural = "主营业务成本报表"

class CostAdjust(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "当期成本调整项"
      verbose_name_plural = "当期成本调整项报表"

class OperatingCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本"
      verbose_name_plural = "运营成本报表"