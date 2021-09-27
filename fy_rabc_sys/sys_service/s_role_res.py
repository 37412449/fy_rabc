# !/usr/bin/env python
# -*- coding: UTF-8 –*-

import json

from fy_rabc_sys.sys_models.model_role import RoleModel
from fy_rabc_sys.sys_models.model_resource import ResourceModel
from fy_rabc_sys.sys_models.model_role_res import RoleResModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.admin_log import AdminLog


class RoleResService:
    __al = AdminLog()

    def __init__(self):
        pass

    def getAllRoles(self):
        reLisRole = []
        reFlag = 0
        reMsg = ''
        try:
            tmpRol = RoleModel.objects.values('role_code', 'role_name').filter(status=1)
            if tmpRol and len(tmpRol) > 0:
                reFlag = 1
                reMsg = '查询成功'
                tmpRol = list(tmpRol)
                for r in tmpRol:
                    reLisRole.append({'code': r['role_code'], 'name': r['role_name']})

            else:
                reFlag = 0
                reMsg = '未查询到任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '查询失败：' + str(e)
            print(str(e))
        finally:
            return reFlag, reMsg, reLisRole

    def getRoleAllRes(self, rolCode):
        reLisRes = []
        reFlag = 0
        reMsg = ''
        try:
            tmpRes = ResourceModel.objects.values('res_code', 'id', 'res_name', 'res_value').filter(
                res_code__in=(RoleResModel.objects.values('res_code').filter(role_code=rolCode))).filter(status=1)
            if tmpRes and len(tmpRes) > 0:
                reFlag = 1
                reMsg = '查询成功'
                tmpRol = list(tmpRes)
                for r in tmpRol:
                    reLisRes.append(r['id'])

            else:
                reFlag = 0
                reMsg = '未查询到任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '查询失败：' + str(e)
            print(str(e))
        finally:
            return reFlag, reMsg, reLisRes

    def saveRolRes(self, request, operator):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                role_code = jsData['role_code']
                ress = jsData['ress']

                # 先删除
                RoleResModel.objects.filter(role_code_id=role_code).delete()

                # 再新增
                for r in ress:
                    uuid = getUUID()
                    role_res_code = 'RO-RE-' + uuid[6:]
                    rr = RoleResModel.objects.create(role_res_code=role_res_code, res_code_id=r, role_code_id=role_code,
                                                     creator=operator)
                reFlag = 1
                reMsg = '更新成功'

                # 日志
                try:
                    self.__al.log_addition(request, rr, '更新成功')
                except Exception as e:
                    print(e)

        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)

        finally:
            return reFlag, reMsg
