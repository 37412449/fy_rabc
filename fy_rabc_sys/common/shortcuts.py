# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.template import loader
from django.shortcuts import HttpResponse
from rest_framework.views import View

from django.conf import settings
from fy_rabc.PermissionManage import PermissionManage
from fy_rabc.common.sys_comm import *

__pm = PermissionManage()


def render(request, template_name, context=None, content_type=None, status=None, using=None):
    if context:
        context['has_add_permission'] = __pm.permissionCheck(request, getPageAction('新增'))
        context['has_change_permission'] = __pm.permissionCheck(request, getPageAction('修改'))
        context['has_delete_permission'] = __pm.permissionCheck(request, getPageAction('删除'))
        context['has_view_permission'] = __pm.permissionCheck(request, getPageAction('查看'))
        context['has_query_permission'] = __pm.permissionCheck(request, getPageAction('查询'))
        context['has_import_permission'] = __pm.permissionCheck(request, getPageAction('导入'))
        context['has_export_permission'] = __pm.permissionCheck(request, getPageAction('导出'))
    else:
        has_add_permission = __pm.permissionCheck(request, getPageAction('新增'))
        has_change_permission = __pm.permissionCheck(request, getPageAction('修改'))
        has_delete_permission = __pm.permissionCheck(request, getPageAction('删除'))
        has_view_permission = __pm.permissionCheck(request, getPageAction('查看'))
        has_query_permission = __pm.permissionCheck(request, getPageAction('查询'))
        has_import_permission = __pm.permissionCheck(request, getPageAction('导入'))
        has_export_permission = __pm.permissionCheck(request, getPageAction('导出'))
        context = {'has_add_permission': has_add_permission, 'has_change_permission': has_change_permission,
                   'has_delete_permission': has_delete_permission, 'has_view_permission': has_view_permission,
                   'has_query_permission': has_query_permission, 'has_import_permission': has_import_permission,
                   'has_export_permission': has_export_permission}

    content = loader.render_to_string(template_name, context, request, using=using)
    return HttpResponse(content, content_type, status)


class SysView(View):
    pm = PermissionManage()

    def __init__(self, **kwargs):
        super(SysView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.

        if request.method.lower() == 'post':
            # 权限判断，如果对应的操作没有权限，则直接返回“权限不足”，如果有，则继续以下分发操作
            flag = -9
            msg = '权限不足'
            try:
                reData = str(request.body, encoding="utf-8")
                jsData = json.loads(reData)
                actionValue = ''
                if 'optype' in jsData.keys():
                    if jsData['optype'] == 'add':
                        actionValue = '新增'
                    elif jsData['optype'] == 'update':
                        actionValue = '修改'
                    elif jsData['optype'] == 'delete':
                        actionValue = '删除'
                    elif jsData['optype'] == 'view':
                        actionValue = '查看'
                    elif jsData['optype'] == 'query':
                        actionValue = '查询'
                    elif jsData['optype'] == 'import':
                        actionValue = '导入'
                    elif jsData['optype'] == 'export':
                        actionValue = '导出'

                    if actionValue == '':
                        msg = '没有对应的权限'
                        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
                    else:
                        auFlag = self.pm.permissionCheck(request, getPageAction(actionValue))
                        if auFlag is False:
                            return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
                else:
                    actionValue = '修改'
                    auFlag = self.pm.permissionCheck(request, getPageAction(actionValue))
                    if auFlag is False:
                        msg = '没有对应的权限'
                        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
            except Exception as e:
                settings.SYS_LOG.logger.error('SysView.dispatch:' + str(e))
                msg = '权限判断异常'
                return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
