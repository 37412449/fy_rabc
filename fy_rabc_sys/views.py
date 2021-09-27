# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

from fy_rabc_sys.sys_service.s_role_res import RoleResService


def test(request):
    return render('test.html', {"msg": 'hello'})


def getPinYin(request):
    flag = 0
    msg = ''
    data = ''
    if request.method == 'POST':
        from xpinyin import Pinyin
        try:
            reData = str(request.body, encoding="utf-8")
            jsData = json.loads(reData)
            chs = str(jsData['data']).strip()
            py = Pinyin()
            data = py.get_pinyin(chs, '')
            flag = 1
            msg = u'转换成功'
        except Exception as e:
            flag = -1
            msg = str(e)

    return HttpResponse(json.dumps({'code': flag, 'msg': msg, 'data': data}), content_type="application/json");
