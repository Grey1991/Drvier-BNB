from django.db import models


# Create your models here.

class Property(models.Model):
    user_ID = models.ForeignKey('UserAndAdmin.User', on_delete=models.CASCADE)
    price = models.FloatField(default=0.0)
    status = models.BooleanField(default=False)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, related_name='Address.address+')
    images = models.ForeignKey('Images', on_delete=models.CASCADE, related_name='Image.images+')
    TYPE_PROPERTY_CHOICES = (
        ('H', 'House'),
        ('A', 'Apartment'),
        ('S', 'Studio'),
        ('O', 'others'),
    )
    types_property = models.CharField(max_length=1, choices=TYPE_PROPERTY_CHOICES, default='O')
    capacity = models.IntegerField(default=0)
    num_bathrooms = models.IntegerField(default=0)
    num_bedroom = models.IntegerField(default=0)

    num_double_bed = models.IntegerField(default=0)
    num_single_bed = models.IntegerField(default=0)
    num_sofa_bed = models.IntegerField(default=0)
    area = models.FloatField(default=0.0)

    kitchen = models.BooleanField(default=False)
    In_unit_washer = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)
    AC = models.BooleanField(default=False)
    TV = models.BooleanField(default=False)
    blower = models.BooleanField(default=False)
    bathtub = models.BooleanField(default=False)

    parking = models.BooleanField(default=False)
    gyms = models.BooleanField(default=False)
    swimming_pools = models.BooleanField(default=False)

    party = models.BooleanField(default=False)
    pet = models.BooleanField(default=False)
    smoking = models.BooleanField(default=False)
    couple = models.BooleanField(default=False)

    longitude = models.FloatField(default=0.0)  # 经度
    latitude = models.FloatField(default=0.0)  # 纬度

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Address(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    postcode = models.IntegerField(default=0)


class Images(models.Model):
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=100)