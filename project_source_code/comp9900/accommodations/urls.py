from django.conf.urls import url
from django.urls import path


from . import views

urlpatterns = [
    url(r'^$', views.user_login, name='login'),

]