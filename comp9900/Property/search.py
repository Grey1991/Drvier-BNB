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

    search_form = forms.SearchForm()

    context = {
        'properties': properties,
        'search_form': search_form
        # 'page_range': page_range
    }

    return render(request, template, context)


def multi_search(request):
    template = 'property_list.html'
    if request.method == "POST":

        search_form = forms.PropertyForm(request.POST)
        if search_form.is_valid():
            user_ID = search_form.cleaned_data['user_ID']
            price = search_form.cleaned_data['price']
            types_property = search_form.cleaned_data['types_property']

            province = search_form.cleaned_data['province']
            city = search_form.cleaned_data['city']
            state = search_form.cleaned_data['state']
            address = search_form.cleaned_data['address']
            postcode = search_form.cleaned_data['postcode']

            capacity = search_form.cleaned_data['capacity']
            num_bathrooms = search_form.cleaned_data['num_bathrooms']
            num_bedrooms = search_form.cleaned_data['num_bedrooms']
            num_double_bed = search_form.cleaned_data['num_double_bed']
            num_single_bed = search_form.cleaned_data['num_single_bed']
            num_sofa_bed = search_form.cleaned_data['num_sofa_bed']
            area = search_form.cleaned_data['area']

            kitchen = search_form.cleaned_data['kitchen']
            in_unit_washer = search_form.cleaned_data['in_unit_washer']
            elevator = search_form.cleaned_data['elevator']
            heating = search_form.cleaned_data['heating']
            ac = search_form.cleaned_data['ac']
            tv = search_form.cleaned_data['tv']
            wifi = search_form.cleaned_data['wifi']
            blower = search_form.cleaned_data['blower']
            bathtub = search_form.cleaned_data['bathtub']

            parking = search_form.cleaned_data['parking']
            gyms = search_form.cleaned_data['gyms']
            swimming_pool = search_form.cleaned_data['swimming_pool']

            party = search_form.cleaned_data['party']
            pet = search_form.cleaned_data['pet']
            smoking = search_form.cleaned_data['smoking']
            couple = search_form.cleaned_data['couple']
            status = search_form.cleaned_data['status']


    else:
        search_form = forms.SearchForm()
        return render(request, template,{'search_form':search_form})
