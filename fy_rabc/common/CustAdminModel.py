# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
from fy_rabc.PermissionManage import PermissionManage

from fy_rabc.common.sys_comm import *


class CustAdminModel(admin.ModelAdmin):
    __pm = PermissionManage()

    def __init__(self, model, admin_site):
        super(CustAdminModel, self).__init__(model, admin_site)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        perFlag = self.__pm.permissionCheck(request, getPageAction('新增'))
        return perFlag

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        perFlag = self.__pm.permissionCheck(request, getPageAction('修改'))
        return perFlag

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        perFlag = self.__pm.permissionCheck(request, getPageAction('删除'))
        return perFlag

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        perFlag = self.__pm.permissionCheck(request, getPageAction('查看'))
        return perFlag

    def has_view_or_change_permission(self, request, obj=None):
        return self.has_view_permission(request, obj) or self.has_change_permission(request, obj)
