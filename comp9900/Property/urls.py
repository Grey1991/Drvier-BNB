from django.conf.urls import url
from . import views
from . import search


app_name = 'property'
urlpatterns = [
    # url(r'^$', views.property_signup, name='welcome'),
    url(r'^$', views.add_property,name="add_property"),
    url(r'^results/', search.simple_search, name="simple_search"),
    url(r'^results/', search.multi_search, name="multi_search"),
]