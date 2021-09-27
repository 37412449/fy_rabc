# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone


class OrgModel(models.Model):
    # parent_id = models.IntegerField(blank=True, null=True, verbose_name=u"父节点ID")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='fk_parent_id', null=True, blank=True,
                               verbose_name='父节点ID')
    org_code = models.CharField(unique=True, max_length=50, verbose_name=u"组织架构代码")
    org_name = models.CharField(max_length=50, verbose_name=u"组织架构名称")

    # ‘C’：公司；‘D’：部门；‘G’：组；‘P’：岗位；
    org_type = models.CharField(max_length=1, verbose_name=u"组织架构类型",
                                choices=(('C', '公司'), ('D', '部门'), ('G', '小组'), ('P', '岗位')), default='D')

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.org_code

    class Meta:
        managed = False
        db_table = 't_sys_org'
        app_label = 'fy_rabc_sys'
        verbose_name = '组织架构管理'
        verbose_name_plural = '组织架构管理'
