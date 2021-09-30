# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.conf import settings
from fy_rabc_sys.sys_models.model_user_role import UserRoleModel
from fy_rabc_sys.sys_models.model_resource import ResourceModel
from fy_rabc_sys.sys_models.model_role_res import RoleResModel


class PermissionManage:

    def __init__(self):
        pass

    def getSuperUserPermis(self):
        lisRes = ResourceModel.objects.values('id', 'parent_id', 'res_code', 'res_type', 'res_name',
                                              'res_value').filter(res_type='A').filter(status=1)
        lisRes = list(lisRes)
        return lisRes

    def getPermission(self, user_code):
        lisRes = ResourceModel.objects.values('id', 'parent_id', 'res_code', 'res_type', 'res_name',
                                              'res_value').filter(res_code__in=(
            RoleResModel.objects.values('res_code').filter(role_code__in=(
                UserRoleModel.objects.values('role_code').filter(user_code=user_code).filter(status=1)).filter(
                status=1))).filter(status=1)).filter(status=1)
        lisRes = list(lisRes)
        return lisRes

    def getAllPermission(self, user_code):
        reAllPer = []
        if user_code == 'superuser':
            lisRes = self.getSuperUserPermis()
        else:
            lisRes = self.getPermission(user_code)
        if lisRes is None or len(lisRes) <= 0:
            return None

        i = 0
        dicAllPer = {i: lisRes}
        lisParId = [a['parent_id'] for a in lisRes]
        lisParId = list(set(lisParId))
        while True:
            if lisParId is None or len(lisParId) <= 0:
                break

            tmpLis = ResourceModel.objects.values('id', 'parent_id', 'res_code', 'res_type', 'res_name',
                                                  'res_value').filter(id__in=(lisParId)).filter(status=1)
            tmpLis = list(tmpLis)
            if tmpLis and len(tmpLis) > 0:
                i += 1
                dicAllPer[i] = tmpLis
                lisParId = [a['parent_id'] for a in tmpLis]
                lisParId = list(set(lisParId))
            else:
                break

        # 排序
        dicAllPer = sorted(dicAllPer.items(), key=lambda x: x[0], reverse=True)

        # 结构简化
        lisAllPer = [x[1] for x in dicAllPer]
        for m in lisAllPer:
            for t in m:
                reAllPer.append(t)

        return reAllPer

    def permissionCheck(self, request, opType):
        """
        权限判断
        :param request: request
        :param opType: 操作类型
        :return: 布尔值
        """
        if opType is None:
            return False
        try:
            lisAllPer = request.session.get("permissions_list")
            reqPath = request.path
            if lisAllPer is None or reqPath is None or len(lisAllPer) <= 0:
                return False
            parMenu = [m for m in lisAllPer if
                       m['res_value'] is not None and str(m['res_value']).strip() != '' and reqPath.find(
                           str(m['res_value'])) >= 0 and m['res_type'] == 'M']
            if parMenu is None or len(parMenu) <= 0:
                return False

            opAll = [m for m in lisAllPer if
                     m['parent_id'] == parMenu[0]['id'] and m['res_type'] == 'A' and str(m['res_value']) == opType]
            if opAll is None or len(opAll) <= 0:
                return False
            else:
                return True
        except Exception as e:
            settings.SYS_LOG.logger.error('permissionCheck:' + str(e))
            return False
