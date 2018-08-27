from django.forms import Textarea,NumberInput
from django import forms
from Property.models import Property,  Images
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class PropertyForm(forms.ModelForm):
    """
    添加房屋表单
    """
    # image = forms.ImageField(required=False)
    class Meta:
        model = Property
        field = exclude = ['created_at', 'updated_at', 'longitude', 'latitude']
        labels = {
            'user_ID': 'Your email',
            'status': 'Release now?',
            'num_bathrooms': 'Number of Bathrooms',
            'num_bedrooms': 'Number of Bedrooms',
            'num_double_bed': 'Number of DoubleBed',
            'num_single_bed': 'Number of SingleBed',
            'num_sofa_bed': 'Number of SofaBed',
            'ac': 'Air Conditioner',
            'tv': 'TV',
            'wifi': 'WIFI',
        }

        # widgets = {
        #     'price': NumberInput(attrs={'class': 'special'}), # 关键是这一行
        # }

# class AddressForm(forms.ModelForm):
#     """
#     添加地址表单
#     """
#     class Meta:
#         model = Address
#         fields = '__all__'

# class ImageForm(forms.ModelForm):
#     """
#     添加图片表单
#     """
#     class Meta:
#         model = Images
#         fields = '__all__'