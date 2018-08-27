from django.conf.urls import url
from . import views



app_name = 'property'
urlpatterns = [
    # url(r'^$', views.property_signup, name='welcome'),
    url(r'^$', views.add_property,name="add_property"),
]