from django.contrib import admin

from fy_rabc_sys.sys_models.model_company import CompanyModel
cm = CompanyModel.objects.values('short_name').filter(status=1)
if cm and len(cm) >= 1:
    admin.site.site_header = cm[0]['short_name']
else:
    admin.site.site_header = '富元证券'

admin.site.site_title = '权限管理系统'
admin.site.index_title = '权限管理系统'
admin.ModelAdmin.list_per_page = 20  # 每页中显示多少条数据
admin.ModelAdmin.actions_on_top = True  # 顶部显示的属性 (“动作”下拉框)
admin.ModelAdmin.actions_on_bottom = False  # 底部显示的属性 (“动作”下拉框)
admin.site.site_url = "/admin"  # 重写“查看站点” 链接

from fy_rabc_sys.sys_admin.admin_config import ConfigAdmin
from fy_rabc_sys.sys_admin.admin_company import CompanyAdmin
from fy_rabc_sys.sys_admin.admin_config import ConfigAdmin
from fy_rabc_sys.sys_admin.admin_org import OrgAdmin
from fy_rabc_sys.sys_admin.admin_resource import ResourceAdmin
from fy_rabc_sys.sys_admin.admin_role import RoleAdmin
from fy_rabc_sys.sys_admin.admin_role_res import RoleResAdmin
from fy_rabc_sys.sys_admin.admin_user import UserAdmin
from fy_rabc_sys.sys_admin.admin_user_role import UserRoleAdmin

