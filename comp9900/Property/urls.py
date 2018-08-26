from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.property_signup, name='add_property'),
]