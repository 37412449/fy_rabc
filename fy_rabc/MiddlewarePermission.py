# !/usr/bin/env python
# -*- coding: UTF-8 –*-

import re
from django.shortcuts import HttpResponse, redirect, render
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class MiddlewarePermission(MiddlewareMixin):
    """
    自定义权限验证中间件
    """

    def process_request(self, request):

        # 1. 白名单验证：当前访问的URL在不在白名单
        for menu in settings.WHITE_URL_LIST:
            ret = re.search(menu, request.path)
            if ret:
                return None

        # 2、验证用户是否已经登录
        user = request.user
        if not user:
            return redirect("login")

        # 3、获取当前用户的所有权限
        permissions_list = request.session.get("permissions_list")
        if permissions_list:

            # 遍历权限列表，匹配当前路径，匹配上放行
            for m in permissions_list:
                if m['res_value'] and str(m['res_value']).strip() != '' and str(m['res_type']) == 'M':
                    url = m['res_value']
                    if re.search(f"^{url}", request.path):
                        return None
        elif permissions_list is None:
            return redirect("login")

        # 没有匹配上，提示没有权限
        return HttpResponse("没有权限")
