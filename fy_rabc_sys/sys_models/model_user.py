# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone

from .model_org import OrgModel


class UserModel(models.Model):
    org_code = models.ForeignKey(OrgModel, models.DO_NOTHING, db_column='org_code', to_field='org_code',
                                 verbose_name=u"组织架构代码")
    user_code = models.CharField(unique=True, max_length=50, verbose_name=u"用户代码")
    user_name = models.CharField(max_length=50, verbose_name=u"用户姓名")
    nick_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"用户昵称")
    ico_img = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"头像图片地址")
    gender = models.IntegerField(blank=True, null=True, verbose_name=u"性别", default=1, choices=((0, '女'), (1, '男')))
    id_num = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"身份证号码")
    tel = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"手机号")
    email = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"E-Mail地址")
    login_name = models.CharField(unique=True, max_length=50, blank=True, null=True, verbose_name=u"登录名")
    pwd = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"登录密码", default='123456')

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.user_name

    class Meta:
        managed = False
        db_table = 't_sys_user'
        app_label = 'fy_rabc_sys'
        verbose_name = '用户信息管理'
        verbose_name_plural = '用户信息管理'
