
from django import forms
from Property.models import Property
from django.contrib.auth.forms import ReadOnlyPasswordHashField
#
# TYPE_PROPERTY_CHOICES = (
#     ('H', 'House'),
#     ('A', 'Apartment'),
#     ('S', 'Studio'),
#     ('O', 'others'),
# )

class PropertyForm(forms.Form):
    """
    添加房屋表单
    """
    class Meta:
        model = Property
        field = {'price', 'types_property', 'capacity', 'area'}


    # price = forms.FloatField(label='Price', required=True)
    # types_property = forms.CharField(label='Type', choices=TYPE_PROPERTY_CHOICES, required=True)
    # capacity = forms.IntegerField(label='Capacity', required=True)
    # area = forms.FloatField(lable='Area', required=True)
    #
    # num_bathrooms = forms.IntegerField(label='Number of Bathrooms', required=True)
    # num_bedrooms = forms.IntegerField(lable='Number of Bedrooms', required=True)
    # num_double_bed = forms.IntegerField(lable='Number of Double Bed', required=True)
    # num_single_bed = forms.IntegerField(lable='Number of Single Bed', required=True)
    # num_sofa_bed = forms.IntegerField(lable='Number of Sofa Bed', required=True)
    #
    # kitchen = forms.BooleanField(label='Kitchen',required=True)
    # In_unit_washer = forms.BooleanField(label='In Unit Washer', required=True)
    # elevator = forms.BooleanField(label='Elevator',required=True)
    # heating = forms.BooleanField(label='Heating',required=True)
    # AC = forms.BooleanField(label='AC',required=True)
    # TV = forms.BooleanField(label='TV',required=True)
    # wifi = forms.BooleanField(label='WIFI',required=True)
    # blower = forms.BooleanField(label='Blower',required=True)
    # bathtub = forms.BooleanField(label='Bathtub',required=True)
    #
    # parking = forms.BooleanField(label='Parking',required=True)
    # gyms = forms.BooleanField(label='Gyms',required=True)
    # swimming_pool = forms.BooleanField(label='Swimming Pool',required=True)
    #
    # party = forms.BooleanField(label='Party',required=True)
    # pet = forms.BooleanField(label='Pet',required=True)
    # smoking = forms.BooleanField(label='Smoking',required=True)
    # couple = forms.BooleanField(label='Couple',required=True)

