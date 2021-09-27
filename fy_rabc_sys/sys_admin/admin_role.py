# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from django import forms
from django.shortcuts import HttpResponse

from fy_rabc_sys.sys_models.model_role import RoleModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.CustAdminModel import CustAdminModel


@admin.register(RoleModel)
class RoleAdmin(CustAdminModel):
    list_display = ['pk', 'role_name', 'status']
    search_fields = ['pk', 'role_name']
    fields = ['role_code', 'role_name', 'status', 'creator', 'createdate', 'updator', 'updatedate', 'remark']  # 详细页面的字段
    list_display_links = ('pk', 'role_name')  # 点击可跳转
    # list_editable = ["role_name"]  # 列表界面可编辑
    readonly_fields = ('role_code', 'creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    list_filter = ('status',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(RoleAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['remark']:
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
            if obj.role_code is None or obj.role_code == '':
                uuid = getUUID()
                obj.role_code = 'ROL-' + uuid[4:]
            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        obj.save()
