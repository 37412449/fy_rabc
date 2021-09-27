# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from fy_rabc_sys.sys_service.s_res import ResServic
from fy_rabc_sys.common.shortcuts import *


class ResGetView(SysView):
    __rs = ResServic()

    def get(self, request):
        resTree = self.__rs.getResTree()
        return render(request, 'res_main.html', {"restree": resTree, "actions": PAGE_ACTION})


class ResSaveView(SysView):
    __rs = ResServic()

    def post(self, request):
        flag = 0
        msg = ''
        restree = {}
        curid = 0
        try:
            flag, msg, curid = self.__rs.saveRes(request, request.user.username)
            if flag == 1:
                restree = self.__rs.getResTree()
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'restree': restree, 'curid': curid}),
                            content_type="application/json");


class ResCheckView(SysView):
    __rs = ResServic()

    def post(self, request):
        flag = 0
        msg = ''
        try:
            flag, msg = self.__rs.checkRes(request)
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json");


class ResDelView(SysView):
    __rs = ResServic()

    def post(self, request):
        flag = 0
        msg = ''
        restree = {}
        try:
            flag, msg = self.__rs.delRes(request)
            if flag == 1:
                restree = self.__rs.getResTree()
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'restree': restree}),
                            content_type="application/json");
