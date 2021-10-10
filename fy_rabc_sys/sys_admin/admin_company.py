# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from django import forms

from fy_rabc_sys.sys_models.model_company import CompanyModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.CustAdminModel import CustAdminModel


@admin.register(CompanyModel)
class CompanyAdmin(CustAdminModel):
    list_display = ['pk', 'short_name', 'full_name', 'address', 'tel', 'status']
    search_fields = ['full_name', 'address', 'core_value']
    fields = ['short_name', 'full_name', 'address', 'tel', 'logo_url', 'core_value',
              'status', 'creator', 'createdate', 'updator', 'updatedate', 'remark']  # 详细页面的字段
    list_display_links = ('pk', 'short_name')  # 点击可跳转
    list_editable = ["full_name"]  # 列表界面可编辑
    readonly_fields = ('company_code', 'creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(CompanyAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['core_value', 'remark']:
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
            if obj.company_code is None or obj.company_code == '':
                uuid = getUUID()
                obj.company_code = 'CP-' + uuid[3:]
            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        obj.save()
