from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from Property import forms, models
# Create your views here.
from Property import forms


def add_property(request):
    if request.method == "POST":
        property_form = forms.PropertyForm(request.POST)
        if property_form.is_valid():
            price = property_form.cleaned_data['price']
            types_property = property_form.cleaned_data['types_property']
            capacity = property_form.cleaned_data['capacity']
            area = property_form.cleaned_data['area']

            num_bathrooms = property_form.cleaned_data['num_bathrooms']
            num_bedrooms = property_form.cleaned_data['num_bedrooms']
            num_double_bed = property_form.cleaned_data['num_double_bed']
            num_single_bed = property_form.cleaned_data['num_single_bed']
            num_sofa_bed = property_form.cleaned_data['num_sofa_bed']

            kitchen = property_form.cleaned_data['kitchen']
            in_unit_washer = property_form.cleaned_data['in_unit_washer']
            elevator = property_form.cleaned_data['elevator']
            heating = property_form.cleaned_data['heating']
            ac = property_form.cleaned_data['ac']
            tv = property_form.cleaned_data['tv']
            wifi = property_form.cleaned_data['wifi']
            blower = property_form.cleaned_data['blower']
            bathtub = property_form.cleaned_data['bathtub']

            parking = property_form.cleaned_data['parking']
            gyms = property_form.cleaned_data['gyms']
            swimming_pool = property_form.cleaned_data['swimming_pool']

            party = property_form.cleaned_data['party']
            pet = property_form.cleaned_data['pet']
            smoking = property_form.cleaned_data['smoking']
            couple = property_form.cleaned_data['couple']

            new_property = models.Property()
            new_property.price = price
            new_property.capacity = capacity
            new_property.types_property = types_property
            new_property.capacity = area

            new_property.num_bathrooms = num_bathrooms
            new_property.num_bedroom = num_bedrooms
            new_property.capacity = num_double_bed
            new_property.capacity = num_single_bed
            new_property.capacity = num_sofa_bed

            new_property.capacity = kitchen
            new_property.capacity = in_unit_washer
            new_property.capacity = elevator
            new_property.capacity = heating
            new_property.capacity = ac
            new_property.capacity = tv
            new_property.capacity = wifi
            new_property.capacity = blower
            new_property.capacity = bathtub

            new_property.capacity = parking
            new_property.capacity = gyms
            new_property.capacity = swimming_pool

            new_property.capacity = party
            new_property.capacity = pet
            new_property.capacity = smoking
            new_property.capacity = couple

            new_property.save()

            return HttpResponseRedirect('/')
    else:
        form = forms.PropertyForm()
        return render(request, 'add_property.html',{'property_form':form})