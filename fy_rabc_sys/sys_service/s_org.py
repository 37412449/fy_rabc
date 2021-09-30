# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.conf import settings
from fy_rabc_sys.sys_models.model_company import CompanyModel
from fy_rabc_sys.sys_models.model_org import OrgModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.admin_log import AdminLog
import json


class OrgService:
    __al = AdminLog()

    def __init__(self):
        pass

    def getCompany(self):
        cm = CompanyModel.objects.filter(status=1)
        if cm and len(cm) > 0:
            return cm[0]
        else:
            return None

    def getOrgTree(self):
        reOrg = []
        cm = self.getCompany()
        if cm:
            tmpCM = {"id": -1, "orgname": cm.short_name, "chilorg": [], "orgtype": "C", "status": 1, "remark": ''}
            reOrg.append(tmpCM)
            om = OrgModel.objects.filter()
            firstOrg = [m for m in om if m.parent_id is None]

            def createTreeNode(parentId, parentOrg, lisAllOrg):
                leftOrg = [m for m in lisAllOrg if m.parent_id == parentId]
                for m in leftOrg:
                    if m.org_type in ('D', 'G'):
                        tmpOrg = {"id": m.id, "orgname": m.org_name, "chilorg": [], "orgtype": m.org_type,
                                  "status": m.status,
                                  "remark": m.remark if m.remark is not None else ''}
                        parentOrg['chilorg'].append(tmpOrg)
                        createTreeNode(m.id, tmpOrg, lisAllOrg)
                    else:
                        parentOrg['chilorg'].append(
                            {"id": m.id, "orgname": m.org_name, "orgtype": m.org_type, "status": m.status,
                             "remark": m.remark if m.remark is not None else ''})

            for o in firstOrg:
                tmpOrg = {"id": o.id, "orgname": o.org_name, "chilorg": [], "orgtype": o.org_type, "status": o.status,
                          "remark": o.remark if o.remark is not None else ''}
                createTreeNode(o.id, tmpOrg, om)
                tmpCM["chilorg"].append(tmpOrg)
        return reOrg

    def saveOrg(self, request, operator):
        reFlag = 0
        reMsg = ''
        currId = 0
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                optype = jsData['optype']
                id = jsData["id"]
                orgname = jsData["orgname"]
                orgtype = jsData["orgtype"]
                status = jsData["status"]
                remark = jsData["remark"]
                orgcode = ''

                # 数据校验
                if orgname is None or str(orgname).strip() == '':
                    reFlag = -1
                    reMsg = '名称不能为空！'
                    return reFlag, reMsg, currId

                if orgtype is None or str(orgtype).strip() not in ['D', 'G', 'P']:
                    reFlag = -1
                    reMsg = '类型选择不正确！'
                    return reFlag, reMsg, currId

                if optype == 'add':
                    uuid = getUUID()
                    if orgtype == 'D':
                        orgcode = 'OGD-' + uuid[4:]
                    elif orgtype == 'G':
                        orgcode = 'OGG-' + uuid[4:]
                    elif orgtype == 'P':
                        orgcode = 'OGP-' + uuid[4:]
                    org = OrgModel.objects.create(parent_id=id if id > 0 else None, org_name=orgname, org_code=orgcode,
                                                  org_type=orgtype, status=status, creator=operator, remark=remark)
                    currId = org.id
                    reFlag = 1
                    reMsg = '新增成功'

                    # 日志
                    try:
                        self.__al.log_addition(request, org, reMsg)
                    except Exception as e:
                        settings.SYS_LOG.logger.error('saveOrg:新增组织架构日志异常：' + str(e))
                elif optype == 'update':
                    om = OrgModel.objects.filter(id=id)
                    om.update(org_name=orgname, org_type=orgtype, status=status, updator=operator, remark=remark)
                    currId = id
                    reFlag = 1
                    reMsg = '更新成功'

                    # 日志
                    try:
                        self.__al.log_change(request, om[0], reMsg)
                    except Exception as e:
                        settings.SYS_LOG.logger.error('saveRes:修改组织架构日志异常：' + str(e))
            else:
                reFlag = 0
                reMsg = '未操作任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)
            settings.SYS_LOG.logger.error('saveRes:' + str(e))
        finally:
            return reFlag, reMsg, currId

    def checkOrg(self, request):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                orgId = jsData['id']

                # 数据校验
                if orgId is None or orgId < 0:
                    reFlag = -1
                    reMsg = '组织机构ID输入不正确！'
                    return reFlag, reMsg

                chiOrgCount = OrgModel.objects.filter(parent_id=orgId).count()
                if chiOrgCount > 0:
                    reFlag = 1
                    reMsg = '该机构存在子机构'
                else:
                    from fy_rabc_sys.sys_models.model_user import UserModel
                    usrCount = UserModel.objects.filter(
                        org_code_id__in=(OrgModel.objects.values('org_code').filter(pk=orgId))).count()
                    if usrCount > 0:
                        reFlag = 1
                        reMsg = '该机构存在用户'
                    else:
                        reFlag = 0
                        reMsg = '该机构不存在子机构（或用户）'
            else:
                reFlag = -1
                reMsg = '未作任何数据检测'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)
            settings.SYS_LOG.logger.error('checkOrg:' + str(e))
        finally:
            return reFlag, reMsg

    def delOrg(self, request):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                orgId = jsData['id']

                # 数据校验
                if orgId is None or orgId < 0:
                    reFlag = -1
                    reMsg = '组织机构ID输入不正确！'
                    return reFlag, reMsg
                om = OrgModel.objects.filter(pk=orgId)

                # 日志
                try:
                    self.__al.log_deletion(request, om[0], '删除组织机构记录,id:' + str(orgId))
                except Exception as e:
                    settings.SYS_LOG.logger.error('delOrg:删除组织机构日志异常' + str(e))

                delFlag = om.delete()
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
            settings.SYS_LOG.logger.error('delOrg:' + str(e))
        finally:
            return reFlag, reMsg
