# !/usr/bin/env python
# -*- coding: UTF-8 –*-

import json

from fy_rabc_sys.sys_models.model_user_role import UserRoleModel
from fy_rabc_sys.sys_models.model_role import RoleModel
from fy_rabc_sys.sys_models.model_user import UserModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.admin_log import AdminLog


class RoleUserService:
    __al = AdminLog()

    def __init__(self):
        pass

    def getAllRols(self):
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

    def getRoleUsers(self, rolCode):
        reLisUsrs = []
        reFlag = 0
        reMsg = ''
        try:
            tmpUsrs = UserModel.objects.values('user_code', 'id', 'user_name').filter(user_code__in=(
                UserRoleModel.objects.values('user_code').filter(role_code=rolCode).filter(status=1)
            ));
            if tmpUsrs and len(tmpUsrs) > 0:
                reFlag = 1
                reMsg = '查询成功'
                tmpRol = list(tmpUsrs)
                for r in tmpRol:
                    reLisUsrs.append(r['user_code'])

            else:
                reFlag = 0
                reMsg = '未查询到任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '查询失败：' + str(e)
            print(str(e))
        finally:
            return reFlag, reMsg, reLisUsrs

    def saveUsrRol(self, request, operator):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            if jsData:
                role_code = jsData['role_code']
                usrs = jsData['users']

                # 先删除
                UserRoleModel.objects.filter(role_code_id=role_code).delete()

                # 再新增
                for r in usrs:
                    uuid = getUUID()
                    user_role_code = 'U-R-' + uuid[4:]
                    ur = UserRoleModel.objects.create(user_role_code=user_role_code, user_code_id=r,
                                                      role_code_id=role_code, creator=operator)

                reFlag = 1
                reMsg = '更新成功'

                # 日志
                try:
                    self.__al.log_addition(request, ur, '更新成功')
                except Exception as e:
                    print(e)

        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)

        finally:
            return reFlag, reMsg
