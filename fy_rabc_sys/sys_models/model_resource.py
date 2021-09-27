# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone

from fy_rabc.common.sys_config import *


class ResourceModel(models.Model):
    #parent_id = models.IntegerField(blank=True, null=True, verbose_name=u"资源父ID")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='fk_parent_id', null=True, blank=True,
                               verbose_name='资源父ID')
    res_code = models.CharField(unique=True, max_length=50, verbose_name=u"资源代码")

    # ‘M’：菜单；‘A’：操作；
    res_type = models.CharField(max_length=10, verbose_name=u"资源类型", default='M',
                                choices=(('M', '菜单'), ('A', '操作')))
    res_name = models.CharField(max_length=50, verbose_name=u"资源名称")

    # 如果是菜单，则为菜单路径，中间菜单可以是空；如果是操作，则为操作代码
    #action = [(v,k) for k,v in PAGE_ACTION.items()]
    res_value = models.CharField(max_length=255, blank=True, null=True, verbose_name=u"资源值")

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.res_name

    class Meta:
        managed = False
        db_table = 't_sys_resource'
        app_label = 'fy_rabc_sys'
        verbose_name = '菜单资源管理'
        verbose_name_plural = '菜单资源管理'
