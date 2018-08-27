from django.shortcuts import render, redirect
from django.http import HttpResponse
from Property import forms, models
from Property import forms
from django.db.models import Q
import time



def simple_search(request):
    template = 'property_list.html'
    query = request.GET.get('q')
    results = models.Property.objects.filter(Q(province__icontains=query) |
                                             Q(city__icontains=query) |
                                             Q(state__icontains=query) |
                                             Q(address__icontains=query)
                                             # Q(postcode__exact=int(query))
                                             ).distinct()

    context = {
        'properties': results
    }

    return render(request, template, context)