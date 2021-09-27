# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.db import models
import django.utils.timezone as timezone


class ConfigModel(models.Model):
    main_type = models.CharField(max_length=20, verbose_name=u"参数主类型")
    name = models.CharField(max_length=50, verbose_name=u"参数名称")

    # ‘str’,'dic','arr'
    value_type = models.CharField(max_length=20, verbose_name=u"参数值类型", default='str',
                                  choices=(('str', '字符串'), ('dic', '字典'), ('arr', '数组')))
    value = models.CharField(max_length=100, blank=True, null=True, verbose_name=u"参数值")

    # 1有效；0无效
    status = models.IntegerField(verbose_name=u"记录状态", default=1, choices=((1, '是'), (0, '否')))
    creator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"创建人")
    createdate = models.DateTimeField(blank=True, null=True, verbose_name=u"创建日期", default=timezone.now)
    updator = models.CharField(max_length=50, blank=True, null=True, verbose_name=u"更新人")
    updatedate = models.DateTimeField(blank=True, null=True, verbose_name=u"更新日期", default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True, verbose_name=u"备注")

    def __str__(self):
        return self.name

    # 值显示
    def val(self):
        if len(self.value) > 60:
            return self.value[0:61] + '...'
        else:
            return self.value

    val.short_description = '参数值'
    val.admin_order_field = 'value'

    class Meta:
        managed = False
        db_table = 't_sys_config'
        app_label = 'fy_rabc_sys'
        verbose_name = '参数配置管理'
        verbose_name_plural = '参数配置管理'
