# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from fy_rabc_sys.sys_models.model_company import CompanyModel
from fy_rabc_sys.sys_models.model_org import OrgModel
from fy_rabc_sys.sys_models.model_user import UserModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.admin_log import AdminLog


class UsrService:
    __al = AdminLog()

    def __init__(self):
        pass

    def getCompany(self):
        cm = CompanyModel.objects.filter(status=1)
        if cm and len(cm) > 0:
            return cm[0]
        else:
            return None

    def getUsrTree(self):
        reOrg = []
        cm = self.getCompany()
        if cm:
            tmpCM = {"id": cm.company_code, "usrname": cm.short_name, "chilusr": [], "usrtype": "C", "org_code": "",
                     "nick_name": "",
                     "gender": "", "id_num": "", "tel": "", "email": "", "login_name": "", "status": 1, "remark": ''}
            reOrg.append(tmpCM)
            om = OrgModel.objects.filter(status=1)
            um = UserModel.objects.filter().all()
            firstOrg = [m for m in om if m.parent_id is None]

            def createTreeNode(parentId, parentOrg):
                leftOrg = [m for m in om if m.parent_id == parentId]
                for m in leftOrg:
                    if m.org_type in ('D', 'G'):
                        tmpOrg = {"id": m.org_code, "usrname": m.org_name, "user_code": "", "chilusr": [],
                                  "usrtype": m.org_type, "org_code": m.org_code, "nick_name": "", "gender": "",
                                  "id_num": "", "tel": "", "email": "", "login_name": "", "status": m.status,
                                  "remark": m.remark if m.remark is not None else ''}
                        parentOrg['chilusr'].append(tmpOrg)
                        createTreeNode(m.id, tmpOrg)
                    else:
                        tmpOrg = {"id": m.org_code, "usrname": m.org_name, "user_code": "", "chilusr": [],
                                  "usrtype": m.org_type, "org_code": m.org_code, "user_name": "", "nick_name": "",
                                  "gender": "", "id_num": "", "tel": "", "email": "", "login_name": "",
                                  "status": m.status, "remark": m.remark if m.remark is not None else ''}
                        parentOrg['chilusr'].append(tmpOrg)

                        orgUsr = [u for u in um if u.org_code_id == m.org_code]
                        for u in orgUsr:
                            tmpUsr = {"id": u.user_code, "usrname": u.user_name, "user_code": u.user_code,
                                      "usrtype": 'U',
                                      "org_code": u.org_code_id,
                                      "nick_name": u.nick_name if u.nick_name is not None else '', "gender": u.gender,
                                      "id_num": u.id_num if u.id_num is not None else '',
                                      "tel": u.tel if u.tel is not None else '',
                                      "email": u.email if u.email is not None else '',
                                      "login_name": u.login_name if u.login_name is not None else '',
                                      "status": u.status, "remark": u.remark if u.remark is not None else ''}
                            tmpOrg['chilusr'].append(tmpUsr)

            for o in firstOrg:
                tmpOrg = {"id": o.org_code, "usrname": o.org_name, "user_code": '', "chilusr": [],
                          "usrtype": o.org_type,
                          "org_code": o.org_code, "nick_name": "", "gender": "", "id_num": "", "tel": "", "email": "",
                          "login_name": "", "status": o.status, "remark": o.remark if o.remark is not None else ''}
                createTreeNode(o.id, tmpOrg)
                tmpCM["chilusr"].append(tmpOrg)
        return reOrg

    def saveUsr(self, request, operator):
        reFlag = 0
        reMsg = ''
        currId = 0
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            if jsData:
                optype = jsData['optype']
                id = jsData["id"]
                org_code = jsData["org_code"]
                user_code = jsData["user_code"]
                user_name = jsData["user_name"]
                nick_name = jsData["nick_name"]
                gender = jsData["gender"]
                id_num = jsData["id_num"]
                tel = jsData["tel"]
                email = jsData["email"]
                login_name = jsData["login_name"]
                status = jsData["status"]
                remark = jsData["remark"]
                rols = jsData['user_roles']

                # 数据校验
                if user_name is None or str(user_name).strip() == '':
                    reFlag = -1
                    reMsg = '姓名不能为空！'
                    return reFlag, reMsg, currId

                if login_name is None or str(login_name).strip() == '':
                    reFlag = -1
                    reMsg = '登录账号不能为空！'
                    return reFlag, reMsg, currId

                if optype == 'add':
                    tmpFlag, _, _ = self.checkLoginNameExist(login_name)
                    if tmpFlag == 1:
                        reFlag = -1
                        reMsg = '登录账号已存在！'
                        return reFlag, reMsg, currId

                if optype == 'add':
                    uuid = getUUID()
                    user_code = 'USR-' + uuid[4:]
                    usr = UserModel.objects.create(org_code_id=org_code, user_code=user_code,
                                                   user_name=user_name, nick_name=nick_name, gender=gender,
                                                   id_num=id_num, tel=tel, email=email, login_name=login_name,
                                                   status=status, creator=operator, remark=remark)
                    # 插入角色
                    if rols and len(rols) > 0:
                        from fy_rabc_sys.sys_models.model_user_role import UserRoleModel
                        for r in rols:
                            uuid = getUUID()
                            user_role_code = 'U-R-' + uuid[4:]
                            ur = UserRoleModel.objects.create(user_role_code=user_role_code, user_code_id=usr.user_code,
                                                              role_code_id=r, creator=operator)

                    # 新增用户
                    from django.contrib.auth.models import User
                    user = User.objects.create_user(login_name, email, usr.pwd)
                    user.is_staff = True
                    user.save()

                    currId = usr.id
                    reFlag = 1
                    reMsg = '新增成功'

                    # 日志
                    try:
                        self.__al.log_addition(request, usr, reMsg)
                    except Exception as e:
                        settings.SYS_LOG.logger.error('saveUsr:添加用户日志异常：' + str(e))

                elif optype == 'update':
                    UserModel.objects.filter(user_code=id).update(org_code_id=org_code, user_name=user_name,
                                                                  nick_name=nick_name, gender=gender, id_num=id_num,
                                                                  tel=tel,
                                                                  email=email, login_name=login_name, status=status,
                                                                  updator=operator, remark=remark)

                    # 修改角色
                    if user_code and str(user_code).strip() != '':
                        from fy_rabc_sys.sys_models.model_user_role import UserRoleModel

                        # 先删除
                        UserRoleModel.objects.filter(user_code_id=user_code).delete()

                        # 再新增
                        for r in rols:
                            uuid = getUUID()
                            user_role_code = 'U-R-' + uuid[4:]
                            ur = UserRoleModel.objects.create(user_role_code=user_role_code, user_code_id=user_code,
                                                              role_code_id=r, creator=operator)

                    currId = id
                    reFlag = 1
                    reMsg = '更新成功'

                    # 日志
                    try:
                        self.__al.log_change(request, ur, reMsg)
                    except Exception as e:
                        settings.SYS_LOG.logger.error('saveUsr:修改用户日志异常：' + str(e))
            else:
                reFlag = 0
                reMsg = '未操作任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)
            settings.SYS_LOG.logger.error('saveUsr:' + str(e))
        finally:
            return reFlag, reMsg, currId

    def usrChgOrgView(self, request):
        reFlag = 0
        reMsg = ''
        currId = 0
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            if jsData:
                optype = jsData['optype']
                id = jsData["id"]
                org_code = jsData["org_code"]
                if optype == 'update':
                    um = UserModel.objects.filter(user_code=id)
                    um.update(org_code_id=org_code)
                    currId = id
                    reFlag = 1
                    reMsg = '更新成功'

                    # 日志
                    try:
                        self.__al.log_change(request, um[0], reMsg)
                    except Exception as e:
                        settings.SYS_LOG.logger.error('usrChgOrgView:修改用户组织架构日志异常：' + str(e))
            else:
                reFlag = 0
                reMsg = '未操作任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)
            settings.SYS_LOG.logger.error('usrChgOrgView:' + str(e))
        finally:
            return reFlag, reMsg, currId

    def getAllRolesViews(self):
        from fy_rabc_sys.sys_models.model_role import RoleModel
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
            settings.SYS_LOG.logger.error('getAllRolesViews:' + str(e))
        finally:
            return reFlag, reMsg, reLisRole

    def getUserAllRoles(self, usrCode):
        from fy_rabc_sys.sys_models.model_role import RoleModel
        from fy_rabc_sys.sys_models.model_user_role import UserRoleModel
        reLisRole = []
        reFlag = 0
        reMsg = ''
        try:
            tmpRol = RoleModel.objects.values('role_code').filter(role_code__in=(
                UserRoleModel.objects.values('role_code').filter(user_code=usrCode).filter(status=1)
            ).filter(status=1))
            if tmpRol and len(tmpRol) > 0:
                reFlag = 1
                reMsg = '查询成功'
                tmpRol = list(tmpRol)
                reLisRole = [r['role_code'] for r in tmpRol]
            else:
                reFlag = 0
                reMsg = '未查询到任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '查询失败：' + str(e)
            settings.SYS_LOG.logger.error('getUserAllRoles:' + str(e))

        finally:
            return reFlag, reMsg, reLisRole

    def checkLoginNameExist(self, loginName):
        existFlag = None
        reFlag = 0
        reMsg = ''
        try:
            usr = UserModel.objects.values('id', 'user_code').filter(login_name=loginName)
            if usr is None or len(usr) <= 0:
                reFlag = 0
                reMsg = '用户登录名不存在!'
                existFlag = False
            else:
                reFlag = 1
                reMsg = '用户登录名已存在!'
                existFlag = True

        except Exception as e:
            reFlag = -1
            reMsg = '查询失败：' + str(e)
            settings.SYS_LOG.logger.error('checkLoginNameExist:' + str(e))

        finally:
            return reFlag, reMsg, existFlag

    def checkUsr(self, request):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                usrId = jsData['id']

                # 数据校验
                if usrId is None or str(usrId).strip() == '':
                    reFlag = -1
                    reMsg = '用户代码输入不正确！'
                    return reFlag, reMsg

                from fy_rabc_sys.sys_models.model_user_role import UserRoleModel
                chiUsrCount = UserRoleModel.objects.filter(user_code_id=usrId).count()
                if chiUsrCount > 0:
                    reFlag = 1
                    reMsg = '该用户已赋相关角色'
                else:
                    from django.contrib.auth.models import User
                    usrCount = User.objects.filter(
                        username__in=(UserModel.objects.values('login_name').filter(user_code=usrId))).filter(
                        last_login__gt='2000-01-01 00:00:00').count()
                    if usrCount > 0:
                        reFlag = 1
                        reMsg = '该用户已经登录过，无法删除'
                    else:
                        reFlag = 0
                        reMsg = '该用户可以删除'
            else:
                reFlag = -1
                reMsg = '未作任何数据检测'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)
            settings.SYS_LOG.logger.error('checkUsr:' + str(e))

        finally:
            return reFlag, reMsg

    def delUsr(self, request):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                usrId = jsData['id']

                # 数据校验
                if usrId is None or str(usrId).strip() == '':
                    reFlag = -1
                    reMsg = '用户代码输入不正确！'
                    return reFlag, reMsg
                um = UserModel.objects.filter(user_code=usrId)

                # 日志
                try:
                    self.__al.log_deletion(request, um[0], '删除用户记录,user_code:' + str(usrId))
                except Exception as e:
                    settings.SYS_LOG.logger.error('delUsr:记录删除用户日志异常：' + str(e))

                delFlag = um.delete()
                if delFlag[0] > 0:
                    reFlag = 1
                    reMsg = '删除成功'
                else:
                    reFlag = 0
                    reMsg = '未删除任何数据'
            else:
                reFlag = 0
                reMsg = '未删除任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)
            settings.SYS_LOG.logger.error('delUsr:' + str(e))
        finally:
            return reFlag, reMsg
