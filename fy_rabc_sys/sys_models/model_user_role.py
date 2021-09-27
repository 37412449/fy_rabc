# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone

from .model_user import UserModel
from .model_role import RoleModel


class UserRoleModel(models.Model):
    user_role_code = models.CharField(unique=True, max_length=50, verbose_name=u"用户角色代码")

    user_code = models.ForeignKey(UserModel, models.DO_NOTHING, related_name='fk_user_code', db_column='user_code',
                                  to_field='user_code', verbose_name=u"用户代码")

    # user_code = models.ManyToManyField(UserModel, verbose_name=u"用户代码", blank=True, db_column='user_code')
    role_code = models.ForeignKey(RoleModel, models.DO_NOTHING, related_name='fk_role_code', db_column='role_code',
                                  to_field='role_code', verbose_name=u"角色代码")

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.user_role_code

    class Meta:
        managed = False
        db_table = 't_sys_user_role'
        app_label = 'fy_rabc_sys'
        verbose_name = '用户角色管理'
        verbose_name_plural = '用户角色管理'
