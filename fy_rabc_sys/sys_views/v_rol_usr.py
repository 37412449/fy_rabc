# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from fy_rabc_sys.sys_service.s_role_usr import RoleUserService
from fy_rabc_sys.sys_service.s_user import UsrService
from fy_rabc_sys.common.shortcuts import *


class RolUsrView(SysView):

    def get(self, request):
        us = UsrService()
        usrTree = us.getUsrTree()
        return render(request, 'role_usr.html', {"usrtree": usrTree})


class GetRoles(SysView):
    __rus = RoleUserService()

    def post(self, request):
        flag = 0
        msg = ''
        lisRoles = []
        try:
            flag, msg, lisRoles = self.__rus.getAllRols()
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'roles': lisRoles}), content_type="application/json");


class getRoleUsers(SysView):
    __rus = RoleUserService()

    def post(self, request):
        flag = 0
        msg = ''
        lisUsers = []
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            flag, msg, lisUsers = self.__rus.getRoleUsers(jsData['rolecode'])
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'usrs': lisUsers}), content_type="application/json");


class saveUsrRol(SysView):
    __rus = RoleUserService()

    def post(self, request):
        flag = 0
        msg = ''
        try:
            flag, msg = self.__rus.saveUsrRol(request, request.user.username)
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json");
