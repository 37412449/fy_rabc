# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from fy_rabc_sys.sys_service.s_org import OrgService
from fy_rabc_sys.common.shortcuts import *


class OrgGetView_bak(SysView):
    __os = OrgService()

    def get(self, request):
        cm = self.__os.getCompany()
        return render(request, 'org_main_bak.html', locals())


class OrgGetView(SysView):
    __os = OrgService()

    def get(self, request):
        orgTree = self.__os.getOrgTree()
        return render(request, 'org_main.html', {"orgtree": orgTree})


class OrgCheckView(SysView):
    __os = OrgService()

    def post(self, request):
        flag = 0
        msg = ''
        try:
            flag, msg = self.__os.checkOrg(request)
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg}), content_type="application/json");


class OrgSaveView(SysView):
    __os = OrgService()

    def post(self, request):
        flag = 0
        msg = ''
        orgtree = {}
        curid = 0
        try:
            flag, msg, curid = self.__os.saveOrg(request, request.user.username)
            if flag == 1:
                orgtree = self.__os.getOrgTree()
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'orgtree': orgtree, 'curid': curid}),
                            content_type="application/json");


class OrgDelView(SysView):
    __os = OrgService()

    def post(self, request):
        flag = 0
        msg = ''
        orgtree = {}
        try:
            flag, msg = self.__os.delOrg(request)
            if flag == 1:
                orgtree = self.__os.getOrgTree()
        except Exception as e:
            print(str(e))
        return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'orgtree': orgtree}),
                            content_type="application/json");
