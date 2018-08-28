from django.conf.urls import url
from . import views
from . import search


app_name = 'property'
urlpatterns = [
    # url(r'^$', views.property_signup, name='welcome'),
    url(r'^$', views.add_property,name="add_property"),
    url(r'^add_success/',views.add_property,name="add_address"),
    url(r'^results/', search.simple_search, name="simple_search"),
    url(r'^multi_results/', search.multi_search, name="multi_search"),
]