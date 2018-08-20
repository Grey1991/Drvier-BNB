'''

视图文件


'''
from django.shortcuts import render
from django.http import HttpResponse
from acommodation.models import *
from datetime import datetime

def mainPage(request):

    return render(request,"register.html")



