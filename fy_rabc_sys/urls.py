# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.urls import path
from django.conf.urls import url, include

from fy_rabc_sys.views import *
from fy_rabc_sys.sys_views.v_org import *
from fy_rabc_sys.sys_views.v_res import *
from fy_rabc_sys.sys_views.v_usr import *
from fy_rabc_sys.sys_views.v_rol_usr import *
from fy_rabc_sys.sys_views.v_rol_res import *

comm_path = r'comm'  # 通用功能接口

org_path = r'org'  # 组织架构主目录(同一页面操作，必须以相同的路径开头，用于权限鉴别)
res_path = r'res'  # 系统资源主目录(同一页面操作，必须以相同的路径开头，用于权限鉴别)
usr_path = r'usr'  # 用户信息主目录(同一页面操作，必须以相同的路径开头，用于权限鉴别)
rol_path = r'rol'  # 角色用户主目录(同一页面操作，必须以相同的路径开头，用于权限鉴别)
r2r_path = r'r2r'  # 角色资源主目录(同一页面操作，必须以相同的路径开头，用于权限鉴别)

urlpatterns = [
    # path('', include(router.urls)),
    path(comm_path + '_ch_py', getPinYin),

    # 组织架构 v_org
    path(org_path, OrgGetView.as_view()),
    path(org_path + r'_save', OrgSaveView.as_view()),
    path(org_path + r'_check', OrgCheckView.as_view()),
    path(org_path + r'_del', OrgDelView.as_view()),

    # 系统资源 v_res
    path(res_path, ResGetView.as_view()),
    path(res_path + r'_save', ResSaveView.as_view()),
    path(res_path + r'_check', ResCheckView.as_view()),
    path(res_path + r'_del', ResDelView.as_view()),

    # 用户信息 v_usr
    path(usr_path, UsrGetView.as_view()),
    path(usr_path + r'_save', UsrSaveView.as_view()),
    path(usr_path + r'_chg_org', UsrChgOrgView.as_view()),
    path(usr_path + r'_getroles', QueryAllRoles.as_view()),
    path(usr_path + r'_getselrol', getUserAllRoles.as_view()),
    path(usr_path + r'_logname_exist', checkLoginNameExist.as_view()),
    path(usr_path + r'_check', UsrCheckView.as_view()),
    path(usr_path + r'_del', UsrDelView.as_view()),

    # 角色用户 v_rol_usr
    path(rol_path, RolUsrView.as_view()),
    path(rol_path + r'_all', GetRoles.as_view()),
    path(rol_path + r'_all_usr', getRoleUsers.as_view()),
    path(rol_path + r'_save_usr', saveUsrRol.as_view()),

    # 角色资源 v_rol_res
    path(r2r_path, RolResView.as_view()),
    path(r2r_path + r's', GetAllRoles.as_view()),
    path(r2r_path + r'_all_res', GetRoleAllRes.as_view()),
    path(r2r_path + r'_save_res', SaveRolRes.as_view()),
]
