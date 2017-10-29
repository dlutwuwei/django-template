# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-28 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u4e1a\u52a1\u62db\u5f85\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u4e1a\u52a1\u62db\u5f85\u8d39',
            },
        ),
        migrations.CreateModel(
            name='CarServiceCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u8f66\u6742\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u8f66\u6742\u8d39',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': '\u9009\u9879',
                'verbose_name_plural': '\u9009\u9879\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u6536\u6b3e\u6c47\u603b',
                'verbose_name_plural': '\u6536\u6b3e\u6c47\u603b\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='CommutingCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u4ea4\u901a\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u4ea4\u901a\u8d39',
            },
        ),
        migrations.CreateModel(
            name='ConferenceTrainingCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u4f1a\u8bae\u57f9\u8bad\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u4f1a\u8bae\u57f9\u8bad\u8d39',
            },
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('changdifei1', models.FloatField(default=0, verbose_name=b'\xe5\x9c\xba\xe5\x9c\xb0\xe8\xb4\xb91')),
                ('changdifei2', models.FloatField(default=0, verbose_name=b'\xe5\x9c\xba\xe5\x9c\xb0\xe8\xb4\xb92')),
                ('changdifei3', models.FloatField(default=0, verbose_name=b'\xe5\x9c\xba\xe5\x9c\xb0\xe8\xb4\xb93')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u4e3b\u8425\u4e1a\u52a1\u6210\u672c',
                'verbose_name_plural': '\u4e3b\u8425\u4e1a\u52a1\u6210\u672c\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='CostAdjust',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u5f53\u671f\u6210\u672c\u8c03\u6574\u9879',
                'verbose_name_plural': '\u5f53\u671f\u6210\u672c\u8c03\u6574\u9879\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='CostRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u6210\u672c\u8d39\u7528\u5360\u6bd4\u9884\u6d4b',
                'verbose_name_plural': '\u6210\u672c\u8d39\u7528\u5360\u6bd4\u9884\u6d4b',
            },
        ),
        migrations.CreateModel(
            name='EmployeeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '\u5458\u5de5\u4eba\u6570\u9884\u6d4b',
                'verbose_name_plural': '\u5458\u5de5\u4eba\u6570\u9884\u6d4b',
            },
        ),
        migrations.CreateModel(
            name='EnlistForcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamItem', models.CharField(default=0, max_length=20, verbose_name=b'\xe8\x80\x83\xe8\xaf\x95\xe9\xa1\xb9\xe7\x9b\xae')),
                ('ExamDetailType', models.CharField(default=0, max_length=20, verbose_name=b'\xe8\x80\x83\xe8\xaf\x95\xe6\x98\x8e\xe7\xbb\x86\xe9\xa1\xb9\xe7\x9b\xae')),
                ('ExamType', models.CharField(default=0, max_length=20, verbose_name=b'\xe8\x80\x83\xe8\xaf\x95\xe7\xb1\xbb\xe5\x9e\x8b')),
                ('ClassType', models.CharField(default=0, max_length=20, verbose_name=b'\xe7\x8f\xad\xe5\x9e\x8b')),
                ('ExamTime', models.DateField(auto_now=True, verbose_name=b'\xe9\xa2\x84\xe8\xae\xa1\xe6\x8b\x9b\xe8\x80\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('StudentEnrollment', models.IntegerField(default=0, verbose_name=b'\xe9\xa2\x84\xe8\xae\xa1\xe4\xba\xba\xe5\xae\xb6\xe6\xb6\x88\xe8\xb4\xb9')),
                ('StudentConsumption', models.IntegerField(default=0, verbose_name=b'\xe9\xa2\x84\xe8\xae\xa1\xe5\xad\xa6\xe8\xb4\xb9\xe6\x94\xb6\xe5\x85\xa5')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
            options={
                'verbose_name': '\u8003\u60c5\u53ca\u62a5\u540d\u6536\u5165\u9884\u6d4b',
                'verbose_name_plural': '\u8003\u60c5\u53ca\u62a5\u540d\u6536\u5165\u9884\u6d4b\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='FixedAssetsInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u56fa\u5b9a\u8d44\u4ea7\u91c7\u8d2d',
                'verbose_name_plural': '\u56fa\u5b9a\u8d44\u4ea7\u91c7\u8d2d',
            },
        ),
        migrations.CreateModel(
            name='IntangibleAssetsInvestment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u65e0\u5f62\u8d44\u4ea7\u91c7\u8d2d',
                'verbose_name_plural': '\u65e0\u5f62\u8d44\u4ea7\u91c7\u8d2d',
            },
        ),
        migrations.CreateModel(
            name='LaborCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u52b3\u52a1\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u52b3\u52a1\u8d39',
            },
        ),
        migrations.CreateModel(
            name='LongTermUnamortizedExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u957f\u671f\u5f85\u644a\u8d39\u7528',
                'verbose_name_plural': '\u957f\u671f\u5f85\u644a\u8d39\u7528',
            },
        ),
        migrations.CreateModel(
            name='OfficeCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u529e\u516c\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u529e\u516c\u8d39',
            },
        ),
        migrations.CreateModel(
            name='PayForAnotherBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u7531\u603b\u90e8\u4ee3\u4e3a\u652f\u4ed8',
                'verbose_name_plural': '\u7531\u603b\u90e8\u4ee3\u4e3a\u652f\u4ed8',
            },
        ),
        migrations.CreateModel(
            name='PayrollCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u85aa\u916c',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u85aa\u916c',
            },
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
                ('changdifei1', models.FloatField(default=0, verbose_name=b'\xe5\x9c\xba\xe5\x9c\xb0\xe8\xb4\xb91')),
                ('changdifei2', models.FloatField(default=0, verbose_name=b'\xe5\x9c\xba\xe5\x9c\xb0\xe8\xb4\xb92')),
                ('changdifei3', models.FloatField(default=0, verbose_name=b'\xe5\x9c\xba\xe5\x9c\xb0\xe8\xb4\xb93')),
                ('province', models.CharField(max_length=200, verbose_name=b'\xe7\x9c\x81\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u5229\u6da6',
                'verbose_name_plural': '\u5229\u6da6\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='PublicityCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u5ba3\u4f20\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u5ba3\u4f20\u8d39',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
                'verbose_name': '\u95ee\u9898\u62a5\u8868',
                'verbose_name_plural': '\u95ee\u9898\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u4e3b\u8425\u4e1a\u52a1\u6536\u5165\u9884\u6d4b',
                'verbose_name_plural': '\u4e3b\u8425\u4e1a\u52a1\u6536\u5165\u9884\u6d4b\u62a5\u8868',
            },
        ),
        migrations.CreateModel(
            name='ServiceCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u670d\u52a1\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u670d\u52a1\u8d39',
            },
        ),
        migrations.CreateModel(
            name='TaxAndExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u7a0e\u91d1\u53ca\u9644\u52a0',
                'verbose_name_plural': '\u7a0e\u91d1\u53ca\u9644\u52a0',
            },
        ),
        migrations.CreateModel(
            name='TelephoneCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u901a\u8baf\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u901a\u8baf\u8d39',
            },
        ),
        migrations.CreateModel(
            name='TotalSpending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u652f\u51fa\u5408\u8ba1',
                'verbose_name_plural': '\u652f\u51fa\u5408\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='TransportationCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u8fd0\u8f93\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u8fd0\u8f93\u8d39',
            },
        ),
        migrations.CreateModel(
            name='TravalCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u5dee\u65c5\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u5dee\u65c5\u8d39',
            },
        ),
        migrations.CreateModel(
            name='UtilitiesCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u6c34\u7535\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u6c34\u7535\u8d39',
            },
        ),
        migrations.CreateModel(
            name='WelfareCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gongwuyuan', models.FloatField(default=0, verbose_name=b'\xe5\x85\xac\xe5\x8a\xa1\xe5\x91\x98')),
                ('shiyedanwei', models.FloatField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('teacher', models.FloatField(default=0, verbose_name=b'\xe6\x95\x99\xe5\xb8\x88')),
                ('month', models.DateTimeField(verbose_name=b'\xe6\x9c\x88\xe4\xbb\xbd')),
            ],
            options={
                'verbose_name': '\u8fd0\u8425\u6210\u672c-\u798f\u5229\u8d39',
                'verbose_name_plural': '\u8fd0\u8425\u6210\u672c-\u798f\u5229\u8d39',
            },
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
