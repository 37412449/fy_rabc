# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from django import forms

from fy_rabc_sys.sys_models.model_role_res import RoleResModel
from fy_rabc.common.sys_comm import *
from fy_rabc_sys.sys_models.model_resource import ResourceModel
from fy_rabc_sys.sys_models.model_role import RoleModel


@admin.register(RoleResModel)
class RoleResAdmin(admin.ModelAdmin):
    list_display = ['pk', 'RoleName', 'ResName', 'status']
    search_fields = ['pk', 'role_code__role_name', 'res_code__res_name']
    fields = ['role_res_code','role_code', 'res_code', 'status', 'creator', 'createdate', 'updator', 'updatedate',
              'remark']  # 详细页面的字段
    list_display_links = ('pk', 'RoleName')  # 点击可跳转
    # list_editable = ["user_role_code"]  # 列表界面可编辑
    readonly_fields = ('creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    def ResName(self, obj):
        res = ResourceModel.objects.values('res_name').filter(res_code=obj.res_code)
        if res and len(res) >= 1:
            return res[0]['res_name']
        else:
            return obj.res_code

    ResName.short_description = '资源名称'

    def RoleName(self, obj):

        rol = RoleModel.objects.values('role_name').filter(role_code=obj.role_code)
        if rol and len(rol) >= 1:
            return rol[0]['role_name']
        else:
            return obj.role_code

    RoleName.short_description = '角色名称'

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(RoleResAdmin, self).formfield_for_dbfield(db_field, **kwargs)
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
            # if obj.role_res_code is None or obj.role_res_code == '':
            uuid = getUUID()
            obj.role_res_code = 'RO-RE-' + uuid[6:]

            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        obj.save()
