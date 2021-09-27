# !/usr/bin/env python
# -*- coding: UTF-8 –*-

import uuid
import json
from ast import literal_eval

from fy_rabc.common.sys_config import *


def getUUID():
    """
    生成UUID
    :return: UUID
    """
    tmpUuid = str(uuid.uuid1())
    tmpUuid = tmpUuid.upper()
    return tmpUuid


def getPageAction(chAction):
    ac = [a for a in PAGE_ACTION if a['value'] == chAction]
    if ac is not None and len(ac) > 0:
        return ac[0]['action']
    else:
        return None


def getConfigByMainType(mainType):
    rePar = {}
    from fy_rabc_sys.sys_models.model_config import ConfigModel
    try:
        cm = ConfigModel.objects.values('main_type', 'name', 'value_type', 'value').filter(main_type=mainType).filter(
            status=1)
        if cm and len(cm) > 0:
            lisConfig = list(cm)
            for p in lisConfig:
                tmpDic = {}
                if p['value_type'].strip().lower() == 'dic':
                    tmpDic[p['name']] = json.loads(p['value'])
                elif p['value_type'].strip().lower() == 'arr':
                    tmpDic[p['name']] = literal_eval(p['value'])
                else:
                    tmpDic[p['name']] = p['value']

                if p['value_type'] not in rePar.keys():
                    rePar[p['main_type']] = tmpDic
                else:
                    rePar[p['main_type']].update(tmpDic)
    except Exception as e:
        print(str(e))
    return rePar


def getConfigByName(name):
    rePar = {}
    from fy_rabc_sys.sys_models.model_config import ConfigModel
    try:
        cm = ConfigModel.objects.values('main_type', 'name', 'value_type', 'value').filter(name=name).filter(
            status=1)
        if cm and len(cm) > 0:
            lisConfig = list(cm)
            for p in lisConfig:
                tmpDic = {}
                if p['value_type'].strip().lower() == 'dic':
                    tmpDic[p['name']] = json.loads(p['value'])
                elif p['value_type'].strip().lower() == 'arr':
                    tmpDic[p['name']] = literal_eval(p['value'])
                else:
                    tmpDic[p['name']] = p['value']

                if p['value_type'] not in rePar.keys():
                    rePar[p['main_type']] = tmpDic
                else:
                    rePar[p['main_type']].update(tmpDic)
    except Exception as e:
        print(str(e))
    return rePar
