# !/usr/bin/env python
# -*- coding: UTF-8 –*-


from fy_rabc_sys.sys_service.s_role_res import RoleResService
from fy_rabc_sys.sys_service.s_res import ResServic

from fy_rabc_sys.common.shortcuts import *


class RolResView(SysView):
    def get(self, request):
        rs = ResServic()
        resTree = rs.getResTree()
        return render(request, 'role_res.html', {"restree": resTree})


class GetAllRoles(SysView):
    __rrs = RoleResService()

    def post(self, request):
        flag = 0
        msg = ''
        lisRoles = []
        try:
            flag, msg, lisRoles = self.__rrs.getAllRoles()
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'roles': lisRoles}), content_type="application/json");


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
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'ress': lisUsers}), content_type="application/json");


class SaveRolRes(SysView):
    __rrs = RoleResService()

    def post(self, request):
        flag = 0
        msg = ''
        try:
            flag, msg = self.__rrs.saveRolRes(request, request.user.username)
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json");
