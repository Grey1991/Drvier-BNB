from django.urls import path


from . import views

urlpatterns = [
    path('', views.mainPage,name = 'main Page'),
]