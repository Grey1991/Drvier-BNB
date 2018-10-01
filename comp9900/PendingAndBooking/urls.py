from django.conf.urls import url
from . import views

app_name = 'PendingAndBooking'
urlpatterns = [
    url(r'^$', views.booking, name='booking'),
    url(r'^(?P<trip_id>[0-9]+)/paynow/', views.paynow, name='paynow'),
    url(r'^(?P<trip_id>[0-9]+)/payment/', views.payment, name='payment'),
    url(r'^trips/', views.trips, name='trips'),
    url(r'^trans/', views.my_trans, name='my_trans'),
    url(r'^(?P<tran_id>[0-9]+)confirm/', views.confirm, name='confirm'),
]