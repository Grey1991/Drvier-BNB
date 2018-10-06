# Generated by Django 2.1 on 2018-10-02 05:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Property', '0002_auto_20180910_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingAndTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('capacity', models.IntegerField(default=0)),
                ('smoking', models.BooleanField(default=False)),
                ('party', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('couple', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TransAndReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(default='Very good!', max_length=500)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('ratings', models.IntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('B', 'Booking'), ('P', 'Pending'), ('C', 'Comfirming'), ('S', 'Success')], default='B', max_length=20)),
                ('position_review', models.IntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comfort_review', models.IntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('price_review', models.IntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('quality_review', models.IntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('contact_name', models.CharField(default='', max_length=500, null=True)),
                ('contact_phone', models.CharField(default='', max_length=10, null=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TransAndReview.pid+', to='Property.Property', verbose_name='owner')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='pendingandtrans',
            name='trans_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PendingAndBooking.TransAndReview'),
        ),
    ]
