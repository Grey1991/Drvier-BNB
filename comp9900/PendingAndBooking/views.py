from django.http import HttpResponse
from django.shortcuts import render, redirect
from Property import models
from PendingAndBooking import models as Pmodels
from django.db.models import Q
import re

# Create your views here.
def booking(request):
    template = 'property_list.html'

    pid = request.POST.get('pid')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    contact_name = request.POST.get('name_booking')
    contact_phone = request.POST.get('Phone_booking')

    pid = int(pid)
    if not check_in:
        print("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print("no check_out")
    else:
        check_out = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_out)

    print("pid {}, check_in {}, check_out {}, contact_name {}, contact_phone {}".format(pid,check_in,check_out,contact_name,contact_phone))

    booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                              Q(end_time__gt=check_in)
                                                              ).values_list('pid', flat=True).distinct()
    for x in booked_properties:
        print('booked id is ',x)

    if pid not in booked_properties:
        tr = Pmodels.TransAndReview()
        tr.user_ID = request.user
        tr.start_time = check_in
        tr.end_time = check_out
        tr.pid = models.Property.objects.get(id= pid)
        tr.contact_name = contact_name
        tr.contact_phone = contact_phone
        tr.save()
        return HttpResponse('succeed')
    else:
        return HttpResponse('failed')


