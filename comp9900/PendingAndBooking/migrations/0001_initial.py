# Generated by Django 2.1 on 2018-09-19 18:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Property', '0002_auto_20180910_1308'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingTrans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('capacity', models.IntegerField(default=0)),
                ('smoking', models.BooleanField(default=False)),
                ('party', models.BooleanField(default=False)),
                ('pet', models.BooleanField(default=False)),
                ('couple', models.BooleanField(default=False)),
                ('blower', models.BooleanField(default=False)),
                ('bathtub', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PendingTrans.pid+', to='Property.Property', verbose_name='owner')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TransAndReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('comment_content', models.CharField(default='', max_length=500)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
                ('ratings', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('B', 'Booking'), ('C', 'Comfirming'), ('S', 'Success')], default='Booking', max_length=1)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TransAndReview.pid+', to='Property.Property', verbose_name='owner')),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
