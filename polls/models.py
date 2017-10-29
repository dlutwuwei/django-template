#coding: utf-8
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from company.models import Company

#class BaseModel(models.Model):

# Create your models here.
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

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
      return self.choice_text
    class Meta:
      verbose_name = "选项"
      verbose_name_plural = "选项报表"

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
class EnlistForcast(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    ExamItem = models.CharField('考试项目',max_length = 20, default=0)
    ExamDetailType = models.CharField('考试明细项目',max_length = 20, default=0)
    ExamType = models.CharField('考试类型',max_length = 20, default=0)
    ClassType = models.CharField('班型',max_length = 20, default=0)
    ExamTime = models.DateField('预计招考时间', auto_now=True)
    StudentEnrollment = models.IntegerField('预计学生消费', default=0)
    StudentConsumption = models.IntegerField('预计学费收入', default=0)
    class Meta:
      verbose_name = "考情及报名收入预测"
      verbose_name_plural = "考情及报名收入预测报表"




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
