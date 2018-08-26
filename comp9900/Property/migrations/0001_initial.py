# Generated by Django 2.1 on 2018-08-26 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('postcode', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('status', models.BooleanField(default=False)),
                ('types_property', models.CharField(choices=[('H', 'House'), ('A', 'Apartment'), ('S', 'Studio'), ('O', 'others')], default='O', max_length=1)),
                ('capacity', models.IntegerField(default=0)),
                ('num_bathrooms', models.IntegerField(default=0)),
                ('num_bedroom', models.IntegerField(default=0)),
                ('num_double_bed', models.IntegerField(default=0)),
                ('num_single_bed', models.IntegerField(default=0)),
                ('num_sofa_bed', models.IntegerField(default=0)),
                ('area', models.FloatField(default=0.0)),
                ('kitchen', models.BooleanField(default=False)),
                ('In_unit_washer', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
                ('heating', models.BooleanField(default=False)),
                ('AC', models.BooleanField(default=False)),
                ('TV', models.BooleanField(default=False)),
                ('blower', models.BooleanField(default=False)),
                ('bathtub', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('gyms', models.BooleanField(default=False)),
                ('swimming_pools', models.BooleanField(default=False)),
                ('party', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('smoking', models.BooleanField(default=False)),
                ('couple', models.BooleanField(default=False)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Address.address+', to='Property.Address')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Image.images+', to='Property.Images')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
