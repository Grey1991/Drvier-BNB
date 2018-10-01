from django.http import HttpResponse
from django.shortcuts import render, redirect
from Property import models
from PendingAndBooking import models as Pmodels
from django.db.models import Q
import re

# Create your views here.
def booking(request):
    template = 'paynow.html'

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
        trans_id = tr.id
        print(trans_id)
        return HttpResponse(trans_id)
    else:
        return HttpResponse('failed')


def paynow(request,trip_id):
    print(trip_id)
    # print("this is here")
    trip = Pmodels.TransAndReview.objects.get(pk=trip_id)
    property = models.Property.objects.get(pk=trip.pid_id)
    # print("price is {}".format(property.price))
    total_money = (trip.end_time-trip.start_time).days * property.price
    # print (total_money)
    return render(request,'paynow.html',{'total_money':total_money, 'trip_id':trip_id})



def payment(request,trip_id):
    template = 'my_trips.html'
    print('here')
    trip = Pmodels.TransAndReview.objects.get(pk=trip_id)
    trip.status = 'C'
    trip.save()
    user_ID = request.user
    trip_list = Pmodels.TransAndReview.objects.filter(Q(user_ID__exact=user_ID)).distinct()
    my_trips = sorted(trip_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trips': my_trips})


def trips(request):
    template = 'my_trips.html'
    user_ID = request.user
    trip_list = Pmodels.TransAndReview.objects.filter(Q(user_ID__exact=user_ID)).distinct()
    my_trips = sorted(trip_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trips':my_trips})

def my_trans(request):
    template = 'my_trans.html'
    user_ID = request.user
    property_list = models.Property.objects.filter(Q(user_ID__exact=user_ID)).values_list('id', flat=True).distinct()
    trans_list = Pmodels.TransAndReview.objects.filter(Q(pid__in=property_list)).distinct()
    my_trans = sorted(trans_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trans':my_trans})

def confirm(request,tran_id):
    tran = Pmodels.TransAndReview.objects.get(pk=tran_id)
    tran.status = 'S'
    tran.save()
    template = 'my_trans.html'
    user_ID = request.user
    property_list = models.Property.objects.filter(Q(user_ID__exact=user_ID)).values_list('id', flat=True).distinct()
    trans_list = Pmodels.TransAndReview.objects.filter(Q(pid__in=property_list)).distinct()
    my_trans = sorted(trans_list, key=lambda x: x.start_time, reverse=True)
    return render(request, template, {'my_trans': my_trans})