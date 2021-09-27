# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib.auth import authenticate
from django.contrib.admin.sites import AdminSite

from fy_rabc.PermissionManage import PermissionManage
from fy_rabc_sys.sys_models.model_user import UserModel


# 登录方法
def mylogin(request):
    if request.method == 'POST':
        try:
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(request=request, username=user_name, password=pass_word)
            if user is not None:
                pm = PermissionManage()
                user_code = ''
                if user.is_superuser:
                    user_code = 'superuser'
                else:
                    um = UserModel.objects.values('user_code').filter(login_name=user_name)
                    if um and len(um) > 0:
                        user_code = um[0]['user_code']

                allPer = pm.getAllPermission(user_code)
                request.session['permissions_list'] = allPer

                # ---------------------------
                # content_type = ContentType.objects.get_for_model(RoleModel)
                # permission = Permission.objects.create(codename='view_role', name='Can view role', content_type=content_type)
                # user.user_permissions.add(permission)
        except Exception as e:
            print(str(e))
    site = AdminSite(name='admin')
    return site.login(request)
