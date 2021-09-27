# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib import admin
import json

from fy_rabc_sys.sys_models.model_resource import ResourceModel
from fy_rabc.common.sys_comm import *
from fy_rabc.common.admin_log import AdminLog


class ResServic:
    __al = AdminLog()

    def __init__(self):
        pass

    def getSiteTitle(self):
        title = admin.site.site_title
        return title

    def getResTree(self):
        reRes = []
        st = self.getSiteTitle()
        if st:
            tmpCM = {"id": -1, "resname": st, "rescode": "", "resvalue": "", "chilres": [], "restype": "S", "status": 1,
                     "remark": ''}
            reRes.append(tmpCM)
            om = ResourceModel.objects.filter()
            firstRes = [m for m in om if m.parent_id is None]

            def createTreeNode(parentId, parentRes, lisAllRes):
                leftRes = [m for m in lisAllRes if m.parent_id == parentId]
                for m in leftRes:
                    if m.res_type in ('M'):
                        tmpRes = {"id": m.id, "resname": m.res_name, "rescode": m.res_code,
                                  "resvalue": m.res_value if m.res_value is not None else '', "chilres": [],
                                  "restype": m.res_type, "status": m.status,
                                  "remark": m.remark if m.remark is not None else ''}
                        parentRes['chilres'].append(tmpRes)
                        createTreeNode(m.id, tmpRes, lisAllRes)
                    else:
                        parentRes['chilres'].append(
                            {"id": m.id, "resname": m.res_name, "rescode": m.res_code,
                             "resvalue": m.res_value if m.res_value is not None else '', "restype": m.res_type,
                             "status": m.status, "remark": m.remark if m.remark is not None else ''})

            for o in firstRes:
                tmpRes = {"id": o.id, "resname": o.res_name, "rescode": o.res_code,
                          "resvalue": o.res_value if o.res_value is not None else '', "chilres": [],
                          "restype": o.res_type, "status": o.status, "remark": o.remark if o.remark is not None else ''}
                createTreeNode(o.id, tmpRes, om)
                tmpCM["chilres"].append(tmpRes)
        return reRes

    def saveRes(self, request, operator):
        reFlag = 0
        reMsg = ''
        currId = 0
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            if jsData:
                optype = jsData['optype']
                id = jsData["id"]
                resname = jsData["resname"]
                restype = jsData["restype"]
                resvalue = jsData['resvalue']
                status = jsData["status"]
                remark = jsData["remark"]

                # 数据校验
                if resname is None or str(resname).strip() == '':
                    reFlag = -1
                    reMsg = '名称不能为空！'
                    return reFlag, reMsg, currId

                if restype is None or str(restype).strip() not in ['M', 'A']:
                    reFlag = -1
                    reMsg = '类型选择不正确！'
                    return reFlag, reMsg, currId

                if optype == 'add':
                    uuid = getUUID()
                    rescode = 'RES-' + uuid[4:]
                    res = ResourceModel.objects.create(parent_id=id if id > 0 else None, res_name=resname,
                                                       res_value=resvalue, res_code=rescode, res_type=restype,
                                                       status=status, creator=operator, remark=remark)
                    currId = res.id
                    reFlag = 1
                    reMsg = '新增成功'

                    # 日志
                    try:
                        self.__al.log_addition(request, res, reMsg)
                    except Exception as e:
                        print(e)
                elif optype == 'update':
                    rm = ResourceModel.objects.filter(id=id)
                    rm.update(res_name=resname, res_type=restype, res_value=resvalue,
                              status=status, updator=operator, remark=remark)
                    currId = id
                    reFlag = 1
                    reMsg = '更新成功'

                    # 日志
                    try:
                        self.__al.log_change(request, rm[0], reMsg)
                    except Exception as e:
                        print(e)
            else:
                reFlag = 0
                reMsg = '未操作任何数据'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)

        finally:
            return reFlag, reMsg, currId

    def checkRes(self, request):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                resId = jsData['id']

                # 数据校验
                if resId is None or resId < 0:
                    reFlag = -1
                    reMsg = '资源ID输入不正确！'
                    return reFlag, reMsg

                chiResCount = ResourceModel.objects.filter(parent_id=resId).count()
                if chiResCount > 0:
                    reFlag = 1
                    reMsg = '该资源存在子资源'
                else:
                    from fy_rabc_sys.sys_models.model_role_res import RoleResModel
                    rrCount = RoleResModel.objects.filter(
                        res_code_id__in=(ResourceModel.objects.values('res_code').filter(pk=resId))).count()
                    if rrCount > 0:
                        reFlag = 1
                        reMsg = '该资源已赋相关角色'
                    else:
                        reFlag = 0
                        reMsg = '该资源不存在子资源（或未赋予给用户）'
            else:
                reFlag = -1
                reMsg = '未作任何数据检测'
        except Exception as e:
            reFlag = -1
            reMsg = '操作异常：' + str(e)

        finally:
            return reFlag, reMsg

    def delRes(self, request):
        reFlag = 0
        reMsg = ''
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)

            if jsData:
                resId = jsData['id']

                # 数据校验
                if resId is None or resId < 0:
                    reFlag = -1
                    reMsg = '资源ID输入不正确！'
                    return reFlag, reMsg
                rm = ResourceModel.objects.filter(pk=resId)

                # 日志
                try:
                    self.__al.log_deletion(request, rm[0], '删除资源记录,id:' + str(resId))
                except Exception as e:
                    print(e)

                delFlag = rm.delete()
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

        finally:
            return reFlag, reMsg
