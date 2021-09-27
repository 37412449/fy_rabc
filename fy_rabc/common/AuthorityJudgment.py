# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.shortcuts import HttpResponse
import json

from fy_rabc.common.sys_comm import *
from fy_rabc.PermissionManage import PermissionManage

pm = PermissionManage()


def AuthJudg(fun):
    def InnerCall(*args, **kwargs):
        try:
            flag = -9
            msg = '权限不足'
            reData = str(args[0].body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData['optype'] == 'add':
                auFlag = pm.permissionCheck(*args, getPageAction('新增'))
                if auFlag is False:
                    return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
            elif jsData['optype'] == 'update':
                auFlag = pm.permissionCheck(*args, getPageAction('修改'))
                if auFlag is False:
                    return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
            elif jsData['optype'] == 'delete':
                auFlag = pm.permissionCheck(*args, getPageAction('删除'))
                if auFlag is False:
                    return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
        except Exception as e:
            msg = '判断权限失败：'
            return HttpResponse(json.dumps({'code': flag, 'msg': msg + str(e)}), content_type="application/json")
        return fun(*args, **kwargs)

    return InnerCall


def AuthJudg_Add(fun):
    def InnerCall(*args, **kwargs):
        try:
            flag = -9
            msg = '权限不足'
            auFlag = pm.permissionCheck(*args, getPageAction('新增'))
            if auFlag is False:
                return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
        except Exception as e:
            msg = '判断权限失败：'
            return HttpResponse(json.dumps({'code': flag, 'msg': msg + str(e)}), content_type="application/json")
        return fun(*args, **kwargs)

    return InnerCall


def AuthJudg_Edit(fun):
    def InnerCall(*args, **kwargs):
        try:
            flag = -9
            msg = '权限不足'
            auFlag = pm.permissionCheck(*args, getPageAction('修改'))
            if auFlag is False:
                return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
        except Exception as e:
            msg = '判断权限失败：'
            return HttpResponse(json.dumps({'code': flag, 'msg': msg + str(e)}), content_type="application/json")
        return fun(*args, **kwargs)

    return InnerCall


def AuthJudg_Delete(fun):
    def InnerCall(*args, **kwargs):
        try:
            flag = -9
            msg = '权限不足'
            auFlag = pm.permissionCheck(*args, getPageAction('删除'))
            if auFlag is False:
                return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
        except Exception as e:
            msg = '判断权限失败：'
            return HttpResponse(json.dumps({'code': flag, 'msg': msg + str(e)}), content_type="application/json")
        return fun(*args, **kwargs)

    return InnerCall


def AuthJudg_View(fun):
    def InnerCall(*args, **kwargs):
        try:
            msg = '权限不足'
            auFlag = pm.permissionCheck(*args, getPageAction('查看'))
            if auFlag is False:
                return HttpResponse(msg)
        except Exception as e:
            msg = '判断权限失败：'
            return HttpResponse(msg)
        return fun(*args, **kwargs)

    return InnerCall
