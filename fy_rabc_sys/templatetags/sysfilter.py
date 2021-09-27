# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django import template
from django.conf import settings

from fy_rabc.common.sys_config import *
from fy_rabc_sys.sys_models.model_org import OrgModel

register = template.Library()


@register.filter(name='suborg')
def suborg(parentId):
    return OrgModel.objects.filter(parent_id=parentId)


@register.filter(name='customtrans')
def customtrans(keyWords):
    try:
        lg = getattr(settings, "LANGUAGE_CODE", "zh-hans")

        if lg == 'zh-hans':
            reValue = TRANS_DICTS[keyWords]
        else:
            reValue = list(TRANS_DICTS.keys())[list(TRANS_DICTS.values()).index(keyWords)]
    except Exception as e:
        reValue = keyWords

    return reValue
