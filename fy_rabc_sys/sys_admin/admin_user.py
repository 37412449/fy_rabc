# !/usr/bin/env python
# -*- coding: UTF-8 –*-


from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

from fy_rabc_sys.sys_models.model_user import UserModel
from fy_rabc.common.sys_comm import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user_code', 'user_name', 'id_num', 'gender', 'status']
    search_fields = ['org_code__org_name', 'user_code', 'user_name']
    fields = ['org_code', 'user_code', 'user_name', 'nick_name', 'ico_img', 'gender', 'id_num', 'tel', 'email',
              'login_name', 'pwd', 'status', 'creator', 'createdate', 'updator', 'updatedate', 'remark']  # 详细页面的字段
    list_display_links = ('pk', 'id_num', 'user_name')  # 点击可跳转
    # list_editable = ["user_code"]  # 列表界面可编辑
    autocomplete_fields = ['org_code']  # 添加选择的搜索框，需要外键字段，并且外键对应的主表中，需要此字段在search_fields中。
    readonly_fields = ('pwd', 'creator', 'createdate', 'updator', 'updatedate')  # 只读字段
    list_filter = ('id_num', 'status')
    # date_hierarchy = 'createdate' # 按日期月份筛选

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(UserAdmin, self).formfield_for_dbfield(db_field, **kwargs)
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
            obj.creator = request.user.username

            # 新增用户
            user = User.objects.create_user(obj.login_name, obj.email, obj.pwd)
            user.is_staff = True
            user.save()
        else:
            obj.updator = request.user.username
        obj.save()
