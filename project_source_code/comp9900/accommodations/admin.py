from django.contrib import admin
from django.contrib.auth.models import Group


from accommodations import models

# 将 model 产生的表 注册到 后台
# 实现 数据库后台的数据操作


admin.site.register(models.User)
admin.site.register(models.UserProfile)
admin.site.unregister(Group)

# admin.site.register(models.Property)
# admin.site.register(models.Address)
# admin.site.register(models.Images)


