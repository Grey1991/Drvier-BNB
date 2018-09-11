from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory

from Property import forms, models
from Property import forms
from .models import Property, Images
from .forms import PropertyForm, ImageForm
import time

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def add_property(request):
    ImageFormSet = modelformset_factory(Images, form=ImageForm)
    if request.method == "POST":
        property_form = forms.PropertyForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        if property_form.is_valid() and formset.is_valid():
            # user_ID = property_form.cleaned_data['user_ID']

            price = property_form.cleaned_data['price']
            types_property = property_form.cleaned_data['types_property']

            province = property_form.cleaned_data['province']
            city = property_form.cleaned_data['city']
            state = property_form.cleaned_data['state']
            address = property_form.cleaned_data['address']
            postcode = property_form.cleaned_data['postcode']

            capacity = property_form.cleaned_data['capacity']
            num_bathrooms = property_form.cleaned_data['num_bathrooms']
            num_bedrooms = property_form.cleaned_data['num_bedrooms']
            num_double_bed = property_form.cleaned_data['num_double_bed']
            num_single_bed = property_form.cleaned_data['num_single_bed']
            num_sofa_bed = property_form.cleaned_data['num_sofa_bed']
            area = property_form.cleaned_data['area']

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
            status = property_form.cleaned_data['status']

            # new_property = models.Property()
            new_property = property_form.save(commit=False)
            new_property.user_ID = request.user
            new_property.price = price
            new_property.types_property = types_property

            new_property.province = province
            new_property.city = city
            new_property.state = state
            new_property.address = address
            new_property.postcode = postcode
            #yguyguyguyg
            #asdasdasdasdasd

            new_property.capacity = capacity
            new_property.num_bathrooms = num_bathrooms
            new_property.num_bedroom = num_bedrooms
            new_property.num_double_bed = num_double_bed
            new_property.num_single_bed = num_single_bed
            new_property.num_sofa_bed = num_sofa_bed
            new_property.area = area

            new_property.kitchen = kitchen
            new_property.in_unit_washer = in_unit_washer
            new_property.elevator = elevator
            new_property.heating = heating
            new_property.ac = ac
            new_property.tv = tv
            new_property.wifi = wifi
            new_property.blower = blower
            new_property.bathtub = bathtub

            new_property.parking = parking
            new_property.gyms = gyms
            new_property.swimming_pool = swimming_pool

            new_property.party = party
            new_property.pet = pet
            new_property.smoking = smoking
            new_property.couple = couple
            new_property.status = status

            # new_property.longitude = 0.0
            # new_property.latitude = 0.0

            new_property.created_at = time.asctime(time.localtime(time.time()))  #
            new_property.updated_at = time.asctime(time.localtime(time.time()))
            new_property.save()

            # album.album_logo = request.FILES['album_logo']
            # file_type = album.album_logo.url.split('.')[-1]
            # file_type = file_type.lower()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'album': album,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
            #     return render(request, 'music/create_album.html', context)

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(pid=new_property, image=image)
                photo.save()
            return render(request, 'add_successfully.html', {'new_property': new_property,'photos':photo})
    else:
        property_form = forms.PropertyForm()
        formset = ImageFormSet(queryset=Images.objects.none())
        return render(request, 'add_property.html', {'property_form': property_form, 'formset': formset})
    # if not request.user.is_authenticated():
    #     return render(request, 'login.html')
    # else:


def property_detail(request, property_id):
    property = Property.objects.get(id=property_id)
    return render(request, 'property_detail.html', {'property': property})


