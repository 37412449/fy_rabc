# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from django import forms
from fy_rabc.common.CustAdminModel import CustAdminModel

from fy_rabc_sys.sys_models.model_config import ConfigModel


@admin.register(ConfigModel)
class ConfigAdmin(CustAdminModel):
    list_display = ['pk', 'main_type', 'name', 'value_type', 'val']
    search_fields = ['main_type', 'name', 'value']
    list_filter = ('main_type', 'status')
    fields = ['main_type', 'name', 'value_type', 'value', 'status', 'creator', 'createdate', 'updator', 'updatedate',
              'remark']  # 详细页面的字段
    list_display_links = ('pk', 'name')  # 点击可跳转
    # list_editable = ["val"]  # 列表界面可编辑
    readonly_fields = ('creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ConfigAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['value', 'remark']:
            # formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            formfield.widget = forms.Textarea(attrs={'cols': '80', 'rows': '5'})
        return formfield

    # 对相关列值进行处理
    def pk(self, obj):
        return str(obj.pk)

    # 列短描述（别名）
    pk.short_description = '主键'

    # 重写保存函数
    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        obj.save()
