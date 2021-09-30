# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.conf import settings
from fy_rabc_sys.sys_service.s_user import UsrService
from fy_rabc.common.AuthorityJudgment import *

from fy_rabc_sys.common.shortcuts import *


class UsrGetView(SysView):
    __us = UsrService()

    def get(self, request):
        try:
            usrTree = self.__us.getUsrTree()
            return render(request, 'user_main.html', {"usrtree": usrTree})
        except Exception as e:
            settings.SYS_LOG.logger.error('UsrGetView:' + str(e))


class UsrSaveView(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        usrtree = {}
        curid = 0
        try:
            flag, msg, curid = self.__us.saveUsr(request, request.user.username)
            if flag == 1:
                usrtree = self.__us.getUsrTree()
        except Exception as e:
            settings.SYS_LOG.logger.error('UsrSaveView:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'usrtree': usrtree, 'curid': curid}),
                            content_type="application/json");


class UsrChgOrgView(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        usrtree = {}
        curid = 0
        try:
            flag, msg, curid = self.__us.usrChgOrgView(request)
            if flag == 1:
                usrtree = self.__us.getUsrTree()
        except Exception as e:
            settings.SYS_LOG.logger.error('UsrChgOrgView:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'usrtree': usrtree, 'curid': curid}),
                            content_type="application/json");


class checkLoginNameExist(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        existflag = None
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            flag, msg, existflag = self.__us.checkLoginNameExist(jsData['loginname'])
        except Exception as e:
            settings.SYS_LOG.logger.error('checkLoginNameExist:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'existflag': existflag}),
                            content_type="application/json");


class QueryAllRoles(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        lisRoles = []
        try:
            flag, msg, lisRoles = self.__us.getAllRolesViews()
        except Exception as e:
            settings.SYS_LOG.logger.error('QueryAllRoles:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'roles': lisRoles}), content_type="application/json");


class getUserAllRoles(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        lisRoles = []
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            flag, msg, lisRoles = self.__us.getUserAllRoles(jsData['usercode'])
        except Exception as e:
            settings.SYS_LOG.logger.error('getUserAllRoles:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'roles': lisRoles}), content_type="application/json");


class UsrCheckView(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        try:
            flag, msg = self.__us.checkUsr(request)
        except Exception as e:
            settings.SYS_LOG.logger.error('UsrCheckView:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json");


class UsrDelView(SysView):
    __us = UsrService()

    def post(self, request):
        flag = 0
        msg = ''
        usrtree = {}
        try:
            flag, msg = self.__us.delUsr(request)
            if flag == 1:
                usrtree = self.__us.getUsrTree()
        except Exception as e:
            settings.SYS_LOG.logger.error('UsrDelView:' + str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'usrtree': usrtree}),
                            content_type="application/json");
