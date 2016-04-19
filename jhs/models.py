# coding=gb2312
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# 保险公司表,存储各家保险公司
class InsureCompany(models.Model):
    """docstring for Insure_Company"""
    # id = models.IntegerField(6)  # 公司ID
    name = models.CharField(max_length=10)  # 公司简称
    fullname = models.CharField(max_length=30, blank=True)  # 公司全面
    url = models.CharField(max_length=50, blank=True)  # 公司主页

    def __unicode__(self):
        return self.name


# 险种列表-与险种费率表一一对应,是分险种的对小单元
class Insure(models.Model):
    """docstring for Insure_Type"""
    # id = models.IntegerField(6)  # 产品ID
    company = models.ForeignKey(InsureCompany)  # 产品公司
    code = models.CharField(max_length=10, blank=True)  # 产品代码
    name = models.CharField(max_length=10)  # 产品简称
    fullname = models.CharField(max_length=30, blank=True)  # 产品全名
    feebase = models.FloatField(max_length=10, default=10000)  # 费率的基准
    minAge = models.SmallIntegerField()  # 最小投保年龄
    maxAge = models.SmallIntegerField()  # 最大投保年龄

    def __unicode__(self):
        return u'%s %s' % (self.code, self.name)


# 险种费率表
class InsureFee(models.Model):
    """docstring for Insure_Fee"""
    insure_code = models.IntegerField(6)  # 产品ID
    sex = models.IntegerField(1)  # 性别
    bxq = models.CharField(max_length=10)  # 保险期间
    lqage = models.CharField(max_length=10)  # 领取年龄
    jfq = models.CharField(max_length=10)  # 交费期间
    major = models.CharField(max_length=10)  # 职业类别
    planN = models.CharField(max_length=10)  # 计划n
    other = models.CharField(max_length=10)  # 其他条件

    age0 = models.FloatField(max_length=10, default=0)  # 被保人投保年龄
    age1 = models.FloatField(max_length=10, default=0)
    age2 = models.FloatField(max_length=10, default=0)
    age3 = models.FloatField(max_length=10, default=0)
    age4 = models.FloatField(max_length=10, default=0)
    age5 = models.FloatField(max_length=10, default=0)
    age6 = models.FloatField(max_length=10, default=0)
    age7 = models.FloatField(max_length=10, default=0)
    age8 = models.FloatField(max_length=10, default=0)
    age9 = models.FloatField(max_length=10, default=0)
    age10 = models.FloatField(max_length=10, default=0)
    age11 = models.FloatField(max_length=10, default=0)
    age12 = models.FloatField(max_length=10, default=0)
    age13 = models.FloatField(max_length=10, default=0)
    age14 = models.FloatField(max_length=10, default=0)
    age15 = models.FloatField(max_length=10, default=0)
    age16 = models.FloatField(max_length=10, default=0)
    age17 = models.FloatField(max_length=10, default=0)
    age18 = models.FloatField(max_length=10, default=0)
    age19 = models.FloatField(max_length=10, default=0)
    age20 = models.FloatField(max_length=10, default=0)
    age21 = models.FloatField(max_length=10, default=0)
    age22 = models.FloatField(max_length=10, default=0)
    age23 = models.FloatField(max_length=10, default=0)
    age24 = models.FloatField(max_length=10, default=0)
    age25 = models.FloatField(max_length=10, default=0)
    age26 = models.FloatField(max_length=10, default=0)
    age27 = models.FloatField(max_length=10, default=0)
    age28 = models.FloatField(max_length=10, default=0)
    age29 = models.FloatField(max_length=10, default=0)
    age30 = models.FloatField(max_length=10, default=0)
    age31 = models.FloatField(max_length=10, default=0)
    age32 = models.FloatField(max_length=10, default=0)
    age33 = models.FloatField(max_length=10, default=0)
    age34 = models.FloatField(max_length=10, default=0)
    age35 = models.FloatField(max_length=10, default=0)
    age36 = models.FloatField(max_length=10, default=0)
    age37 = models.FloatField(max_length=10, default=0)
    age38 = models.FloatField(max_length=10, default=0)
    age39 = models.FloatField(max_length=10, default=0)
    age40 = models.FloatField(max_length=10, default=0)
    age41 = models.FloatField(max_length=10, default=0)
    age42 = models.FloatField(max_length=10, default=0)
    age43 = models.FloatField(max_length=10, default=0)
    age44 = models.FloatField(max_length=10, default=0)
    age45 = models.FloatField(max_length=10, default=0)
    age46 = models.FloatField(max_length=10, default=0)
    age47 = models.FloatField(max_length=10, default=0)
    age48 = models.FloatField(max_length=10, default=0)
    age49 = models.FloatField(max_length=10, default=0)
    age50 = models.FloatField(max_length=10, default=0)
    age51 = models.FloatField(max_length=10, default=0)
    age52 = models.FloatField(max_length=10, default=0)
    age53 = models.FloatField(max_length=10, default=0)
    age54 = models.FloatField(max_length=10, default=0)
    age55 = models.FloatField(max_length=10, default=0)
    age56 = models.FloatField(max_length=10, default=0)
    age57 = models.FloatField(max_length=10, default=0)
    age58 = models.FloatField(max_length=10, default=0)
    age59 = models.FloatField(max_length=10, default=0)
    age60 = models.FloatField(max_length=10, default=0)
    age61 = models.FloatField(max_length=10, default=0)
    age62 = models.FloatField(max_length=10, default=0)
    age63 = models.FloatField(max_length=10, default=0)
    age64 = models.FloatField(max_length=10, default=0)
    age65 = models.FloatField(max_length=10, default=0)
    age66 = models.FloatField(max_length=10, default=0)
    age67 = models.FloatField(max_length=10, default=0)
    age68 = models.FloatField(max_length=10, default=0)
    age69 = models.FloatField(max_length=10, default=0)
    age70 = models.FloatField(max_length=10, default=0)
    age71 = models.FloatField(max_length=10, default=0)
    age72 = models.FloatField(max_length=10, default=0)
    age73 = models.FloatField(max_length=10, default=0)
    age74 = models.FloatField(max_length=10, default=0)
    age75 = models.FloatField(max_length=10, default=0)
    age76 = models.FloatField(max_length=10, default=0)
    age77 = models.FloatField(max_length=10, default=0)
    age78 = models.FloatField(max_length=10, default=0)
    age79 = models.FloatField(max_length=10, default=0)
    age80 = models.FloatField(max_length=10, default=0)

    def __unicode__(self):
        return self.insure_code
