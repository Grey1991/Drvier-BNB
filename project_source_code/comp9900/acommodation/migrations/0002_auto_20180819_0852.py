# Generated by Django 2.0.5 on 2018-08-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acommodation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lodging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_email',
        ),
    ]
