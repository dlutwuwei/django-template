# coding: utf-8

from django.db import models

from django.contrib.auth.models import User



class School(models.Model):
    school_name = models.CharField('分校名称', max_length=200)
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
    company_name = models.CharField('分公司名称', max_length=200)
    company_code = models.CharField('分公司代码', max_length=6, unique=True)
    def __str__(self):
      return self.company_name
    class Meta:
      verbose_name = '分公司设置'
      verbose_name_plural = '分公司设置'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="分公司",
    )
    def __str__(self):
      return self.user.username
