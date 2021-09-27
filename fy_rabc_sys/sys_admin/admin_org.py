# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from django import forms

from fy_rabc_sys.sys_models.model_org import OrgModel
from fy_rabc.common.sys_comm import *


@admin.register(OrgModel)
class OrgAdmin(admin.ModelAdmin):
    list_display = ['pk', 'parent', 'org_code', 'org_name', 'status']
    search_fields = ['pk', 'org_code', 'org_name']
    fields = ['parent', 'org_code', 'org_name', 'org_type', 'status', 'creator', 'createdate', 'updator',
              'updatedate', 'remark']  # 详细页面的字段
    list_display_links = ('pk', 'org_code')  # 点击可跳转
    list_editable = ["org_name"]  # 列表界面可编辑
    readonly_fields = ('org_code', 'creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(OrgAdmin, self).formfield_for_dbfield(db_field, **kwargs)
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
            if obj.org_code is None or obj.org_code == '':
                uuid = getUUID()
                if obj.org_type == 'C':
                    obj.org_code = 'OGC-' + uuid[4:]
                elif obj.org_type == 'D':
                    obj.org_code = 'OGD-' + uuid[4:]
                elif obj.org_type == 'G':
                    obj.org_code = 'OGG-' + uuid[4:]
                elif obj.org_type == 'P':
                    obj.org_code = 'OGP-' + uuid[4:]
                else:
                    obj.org_code = 'OG-' + uuid[3:]
            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        obj.save()
