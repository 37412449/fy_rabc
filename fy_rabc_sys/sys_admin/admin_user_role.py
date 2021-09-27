# !/usr/bin/env python
# -*- coding: UTF-8 –*-


from django.contrib import admin
from django import forms

from fy_rabc_sys.sys_models.model_user_role import UserRoleModel
from fy_rabc_sys.sys_models.model_user import UserModel
from fy_rabc_sys.sys_models.model_role import RoleModel
from fy_rabc.common.sys_comm import *


@admin.register(UserRoleModel)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user_role_code', 'userName', 'roleName', 'status']
    search_fields = ['pk','user_role_code', 'user_code__user_name','role_code__role_name']
    fields = ['user_role_code', 'user_code', 'role_code', 'status', 'creator', 'createdate', 'updator', 'updatedate',
              'remark']  # 详细页面的字段
    list_display_links = ('pk', 'user_role_code')  # 点击可跳转
    # list_editable = ["user_code"]  # 列表界面可编辑
    readonly_fields = ('user_role_code', 'creator', 'createdate', 'updator', 'updatedate')  # 只读字段

    #filter_horizontal =('user_code',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(UserRoleAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in ['remark']:
            # formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
            formfield.widget = forms.Textarea(attrs={'cols': '80', 'rows': '5'})
        return formfield

    # 对相关列值进行处理
    def pk(self, obj):
        return str(obj.pk)

    # 列短描述（别名）
    pk.short_description = '主键'

    def userName(self, obj):
        user = UserModel.objects.values('user_name').filter(user_code=obj.user_code)
        if user and len(user) >= 1:
            return user[0]['user_name']
        else:
            return obj.user_code

    userName.short_description = '用户姓名'

    def roleName(self, obj):
        role = RoleModel.objects.values('role_name').filter(role_code=obj.role_code)
        if role and len(role) >= 1:
            return role[0]['role_name']
        else:
            return obj.role_code

    roleName.short_description = '角色名称'

    # 重写保存函数
    def save_model(self, request, obj, form, change):
        if not change:
            if obj.user_role_code is None or obj.user_role_code == '':
                uuid = getUUID()
                obj.user_role_code = 'U-R-' + uuid[4:]
            obj.creator = request.user.username
        else:
            obj.updator = request.user.username
        # super().save_model(request, obj, form, change)
        '''
        user = UserModel.objects.filter(user_code='10002')
        role = RoleModel.objects.filter(role_code='R_01')
        UserRoleModel.objects.create(user_code=user[0],role_code=role[0],creator='mypc',user_role_code='R_U_02')
        '''
        obj.save()
