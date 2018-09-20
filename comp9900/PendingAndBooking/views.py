from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def booking(request):
    if_login = int(request.POST.get('room_type',None))
    print(if_login)
    if if_login == 0:
        return HttpResponse("Please login before booking")
    else:
        return HttpResponse("paynow")
    # email = request.POST.get('email_booking')
    # print(email)
    # return HttpResponse(email)
