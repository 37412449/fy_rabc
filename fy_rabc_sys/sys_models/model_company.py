# !/usr/bin/env python
# -*- coding: UTF-8 –*-


from django.db import models
import django.utils.timezone as timezone


class CompanyModel(models.Model):
    company_code = models.CharField(max_length=50, verbose_name=u"公司代码")
    short_name = models.CharField(max_length=50, verbose_name=u"公司简称")
    full_name = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"公司全称")
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"公司地址")
    tel = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"公司电话")
    logo_url = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"logo地址")
    core_value = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"核心价值观")

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.short_name

    class Meta:
        managed = False
        db_table = 't_sys_company'
        app_label = 'fy_rabc_sys'
        verbose_name = '公司信息管理'
        verbose_name_plural = '公司信息管理'
