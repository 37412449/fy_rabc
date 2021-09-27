# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone

from .model_resource import ResourceModel
from .model_role import RoleModel


class RoleResModel(models.Model):
    role_res_code = models.CharField(unique=True, max_length=50, verbose_name=u"角色资源代码")
    role_code = models.ForeignKey(RoleModel, models.DO_NOTHING, db_column='role_code', related_name='fk_role_res_rol',
                                  to_field='role_code', verbose_name=u"角色代码")

    res_code = models.ForeignKey(ResourceModel, models.DO_NOTHING, db_column='res_code', related_name='fk_role_res_res',
                                 to_field='res_code', verbose_name=u"资源代码")

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return str(self.pk)

    class Meta:
        managed = False
        db_table = 't_sys_role_res'
        app_label = 'fy_rabc_sys'
        verbose_name = '角色资源管理'
        verbose_name_plural = '角色资源管理'
