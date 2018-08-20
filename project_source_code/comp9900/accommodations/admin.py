from django.contrib import admin

# Register your models here.


# 将 model 产生的表 注册到 后台
# 实现 数据库后台的数据操作



from accommodations import models

admin.site.register(models.User)
admin.site.register(models.UserProfile)
