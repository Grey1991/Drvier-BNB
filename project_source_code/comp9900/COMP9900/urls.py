"""COMP9900 URL Configuration
URL 申明
网站的目录

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from accommodations import views

'''
include() 允许引用其他的 URLconfs 

path() 有四个参数 
route ： 正则表达式 匹配URL准则 -》 遍历 urlpatterns 直到找到匹配项目
不会匹配 post get 参数 or  域名

view 找到 URL 后 调用 view function 
传入 HttpRequset object 

kwargs : dict() -> view function
name 
'''


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('mainpage/',include('accommodations.urls')),
    url(r'^admin/',admin.site.urls),
    url(r'^$', include("accommodations.urls")),
    url(r'^login/', views.user_login),
    url(r'^index/', views.mainPage),

]




