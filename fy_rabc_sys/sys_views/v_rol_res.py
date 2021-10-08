# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.conf import settings
from fy_rabc_sys.sys_service.s_role_res import RoleResService
from fy_rabc_sys.sys_service.s_res import ResServic

from fy_rabc_sys.common.shortcuts import *


class RolResView(SysView):
    def get(self, request):
        try:
            rs = ResServic()
            resTree = rs.getResTree()
            return render(request, 'role_res.html', {"restree": resTree})
        except Exception as e:
            settings.SYS_LOG.logger.error('RolResView:' + str(e))


class GetResTree(SysView):

    def post(self, request):
        restree = []
        try:
            rs = ResServic()
            restree = rs.getResTree()
            flag = 1
            msg = '获取资源成功'

        except Exception as e:
            flag = -1
            msg = '获取资源树异常:' + str(e)
            settings.SYS_LOG.logger.error('GetResTree:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'restree': restree}),
                            content_type="application/json")


class GetAllRoles(SysView):
    __rrs = RoleResService()

    def post(self, request):
        flag = 0
        msg = ''
        lisRoles = []
        try:
            flag, msg, lisRoles = self.__rrs.getAllRoles()

        except Exception as e:
            settings.SYS_LOG.logger.error('GetAllRoles:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'roles': lisRoles}), content_type="application/json")


class GetRoleAllRes(SysView):
    __rrs = RoleResService()

    def post(self, request):
        flag = 0
        msg = ''
        lisUsers = []
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            flag, msg, lisUsers = self.__rrs.getRoleAllRes(jsData['rolecode'])

        except Exception as e:
            settings.SYS_LOG.logger.error('GetRoleAllRes:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'ress': lisUsers}), content_type="application/json")


class SaveRolRes(SysView):
    __rrs = RoleResService()

    def post(self, request):
        flag = 0
        msg = ''
        try:
            flag, msg = self.__rrs.saveRolRes(request, request.user.username)

        except Exception as e:
            settings.SYS_LOG.logger.error('SaveRolRes:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json")
