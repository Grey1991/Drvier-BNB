from django.http import HttpResponse
from django.shortcuts import render, redirect
from Property import models
from PendingAndBooking import models as Pmodels
from django.db.models import Q
import re

# Create your views here.
def booking(request):
    template = 'property_list.html'

    pid = request.POST.get('property_id')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    contact_name = request.POST.get('name_booking')
    contact_phone = request.POST.get('Phone_booking')

    if not check_in:
        print("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print("no check_out")
    else:
        check_out = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_out)

    print("pid {}, check_in {}, check_out {}, contact_name {}, contact_phone {}".format(pid,check_in,check_out,contact_name,contact_phone))

    tr = Pmodels.TransAndReview()








    booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                              Q(end_time__gt=check_in)
                                                              ).values_list('pid', flat=True).distinct()

    for x in booked_properties:
        print('booked id is ', x)


    return HttpResponse("1")
