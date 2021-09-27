# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone

from .model_user import UserModel


class RoleModel(models.Model):
    role_code = models.CharField(unique=True, max_length=50, verbose_name=u"角色代码")
    role_name = models.CharField(max_length=50, verbose_name=u"角色名称")

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.role_name

    class Meta:
        managed = False
        db_table = 't_sys_role'
        app_label = 'fy_rabc_sys'
        verbose_name = '角色信息管理'
        verbose_name_plural = '角色信息管理'
