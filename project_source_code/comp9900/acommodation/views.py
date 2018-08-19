'''

视图文件


'''
from django.shortcuts import render
from django.http import HttpResponse
from acommodation.models import *
from datetime import datetime
# Create your views here.
def mainPage(request):


    # u1 = User(first_name="kai",last_name="fang",user_email="kevifunau@gmail.com",user_password="11111111",gender='M',\
    #           birthdate=datetime(year=1994,month=6,day=21))
    # u1.save()
    return HttpResponse()
