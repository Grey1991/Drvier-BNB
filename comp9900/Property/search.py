from django.shortcuts import render, redirect
from Property import forms, models
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def simple_search(request):
    template = 'property_list.html'
    query = request.GET.get('q')
    property_list = models.Property.objects.filter(Q(province__icontains=query) |
                                             Q(city__icontains=query) |
                                             Q(state__icontains=query) |
                                             Q(address__icontains=query)
                                             # Q(postcode__exact=int(query))
                                             ).distinct()

    # 分页-----------------
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    # index = properties.number - 1
    # max_index = len(paginator.page_range)
    # start_index = index - 5 if index >= 5 else 0
    # end_index = index + 5 if index <= max_index else max_index
    # page_range = paginator.page_range[start_index:end_index]

    context = {
        'properties': properties,
        # 'page_range': page_range
    }

    return render(request, template, context)