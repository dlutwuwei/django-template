#coding: utf-8
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from company.models import Branch, Company, ExamDetailItem, ExamItem, ExamType, ClassType, ProductType, IncomeConversion

from django.utils.dates import MONTHS
from smart_selects.db_fields import ChainedForeignKey

class BaseModelMixin(models.Model,):
  year = models.IntegerField('年份', default=2018)
  company = models.ForeignKey(Company, verbose_name="分公司")
  branch = ChainedForeignKey(
    Branch,
    chained_field='company',
    chained_model_field='company',
    show_all=False,
    auto_choose=True,
    sort=True,
    null=True,
    on_delete=models.SET_NULL,
    verbose_name='所属分部'
  )
  class Meta:
       abstract = True

# 利润表
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

# 考情及报名收入预测
class EnlistForcast(BaseModelMixin):
    # month = models.IntegerField('月份', max_length = 20, choices=MONTHS.items(), default=1)
    examItem = models.ForeignKey(ExamItem, verbose_name ='考试项目', max_length = 20, default=1)
    productType = models.ForeignKey(ProductType, verbose_name='产品类型', max_length = 20, default=1)
    examDetailItem = ChainedForeignKey(
      ExamDetailItem,
      chained_field='examItem',
      chained_model_field="item",
      show_all=False,
      auto_choose=True,
      sort=True,
      null=True,
      on_delete=models.SET_NULL,
      verbose_name="考试明细项目",
    )
    examType = models.ForeignKey(ExamType, verbose_name = '考试类型',max_length = 20, default=1)
    classType = models.ForeignKey(ClassType, verbose_name = '班型', max_length = 20, default=1)
    examTime = models.IntegerField('预计招考时间', choices=MONTHS.items(), default=1)
    studentConsumption = models.FloatField('预计学生消费', default=0)
    studentCount = models.IntegerField('预计招收人数', default=0)
    conversion = models.ForeignKey(
      IncomeConversion,
      verbose_name='转化率',
      max_length = 20,
      null=True,
      blank=True,
      default=None
    )
    class Meta:
      verbose_name = "考情及报名收入预测"
      verbose_name_plural = "考情及报名收入预测报表"
      unique_together = ('year','company','branch', 'examItem', 'examDetailItem','examType', 'classType', 'examTime', 'productType')
      permissions = (
          ('view_enlist', 'Can view enlist'),
      )
    def company_show(self):
      return self.company.company_name
    company_show.short_description = '分公司'


# 主营业务成本
class Cost(models.Model):
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

# 运营成本-薪酬
class PayrollCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-薪酬"
      verbose_name_plural = "运营成本-薪酬"

# 运营成本-薪酬
class OfficeCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-办公费"
      verbose_name_plural = "运营成本-办公费"

# 运营成本-福利费
class WelfareCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-福利费"
      verbose_name_plural = "运营成本-福利费"

# 运营成本-车杂费
class CarServiceCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-车杂费"
      verbose_name_plural = "运营成本-车杂费"

# 运营成本-宣传费
class PublicityCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-宣传费"
      verbose_name_plural = "运营成本-宣传费"

# 运营成本-会议培训费
class ConferenceTrainingCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-会议培训费"
      verbose_name_plural = "运营成本-会议培训费"

# 运营成本-差旅费
class TravalCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-差旅费"
      verbose_name_plural = "运营成本-差旅费"

# 运营成本-服务费
class ServiceCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-服务费"
      verbose_name_plural = "运营成本-服务费"

# 运营成本-水电费
class UtilitiesCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-水电费"
      verbose_name_plural = "运营成本-水电费"

# 运营成本-业务招待费
class BusinessCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-业务招待费"
      verbose_name_plural = "运营成本-业务招待费"

# 运营成本-交通费
class CommutingCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-交通费"
      verbose_name_plural = "运营成本-交通费"

# 运营成本-运输费
class TransportationCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-运输费"
      verbose_name_plural = "运营成本-运输费"

# 运营成本-通讯费
class TelephoneCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-通讯费"
      verbose_name_plural = "运营成本-通讯费"

# 运营成本-劳务费
class LaborCost(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "运营成本-劳务费"
      verbose_name_plural = "运营成本-劳务费"

# 固定资产采购
class FixedAssetsInvestment(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "固定资产采购"
      verbose_name_plural = "固定资产采购"

# 无形资产采购
class IntangibleAssetsInvestment(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "无形资产采购"
      verbose_name_plural = "无形资产采购"

# 长期待摊费用
class LongTermUnamortizedExpenses(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "长期待摊费用"
      verbose_name_plural = "长期待摊费用"

# 由总部代为支付
class PayForAnotherBy(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "由总部代为支付"
      verbose_name_plural = "由总部代为支付"

# 支出合计
class TotalSpending(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "支出合计"
      verbose_name_plural = "支出合计"

# 成本费用占比预测
class CostRatio(models.Model):
    class Meta:
      verbose_name = '成本费用占比预测'
      verbose_name_plural = '成本费用占比预测'

# 员工人数预测
class EmployeeCount(models.Model):
    class Meta:
      verbose_name = '员工人数预测'
      verbose_name_plural = '员工人数预测'

# 主营业务收入预测
class Revenue(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "主营业务收入预测"
      verbose_name_plural = '主营业务收入预测报表'

# 收款
class Collection(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "收款汇总"
      verbose_name_plural = "收款汇总报表"

# 税金及附加
class TaxAndExtra(models.Model):
    gongwuyuan = models.FloatField('公务员', default=0)
    shiyedanwei = models.FloatField('事业单位', default=0)
    teacher = models.FloatField('教师', default=0)
    month = models.DateTimeField('月份')
    class Meta:
      verbose_name = "税金及附加"
      verbose_name_plural = "税金及附加"
