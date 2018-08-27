from django.forms import Textarea
from django import forms
from Property.models import Property, Address, Images
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class PropertyForm(forms.ModelForm):
    """
    添加房屋表单
    """
    class Meta:
        model = Property
        field = exclude = ['created_at', 'updated_at', 'longitude', 'latitude']

        labels = {
            'user_ID': 'Your email',
            'status': 'Release now?',
            'num_bathrooms': 'number of bathrooms',
            'num_bedrooms': 'number of bedrooms',
            'num_double_bed': 'number of double bed',
            'num_single_bed': 'number of single bed',
            'num_sofa_bed': 'number of sofa bed',
        }


class AddressForm(forms.ModelForm):
    """
    添加地址表单
    """
    class Meta:
        model = Address
        fields = '__all__'

class ImageForm(forms.ModelForm):
    """
    添加地址表单
    """
    class Meta:
        model = Images
        fields = '__all__'