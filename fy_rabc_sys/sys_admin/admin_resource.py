# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from django import forms

from fy_rabc_sys.sys_models.model_resource import ResourceModel
from fy_rabc.common.sys_comm import *


@admin.register(ResourceModel)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['pk', 'parent', 'res_code', 'res_type', 'res_name', 'res_value', 'status']
    search_fields = ['pk', 'res_code', 'res_name', 'res_type']
    fields = ['parent', 'res_code', 'res_type', 'res_name', 'res_value', 'status', 'creator', 'createdate',
              'updator', 'updatedate', 'remark']  # 详细页面的字段
    list_display_links = ('pk', 'res_code')  # 点击可跳转
    list_editable = ["res_name"]  # 列表界面可编辑
    readonly_fields = ('res_code', 'creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ResourceAdmin, self).formfield_for_dbfield(db_field, **kwargs)
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
            if obj.res_code is None or obj.res_code == '':
                uuid = getUUID()
                obj.res_code = 'RES-' + uuid[4:]
            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        obj.save()
