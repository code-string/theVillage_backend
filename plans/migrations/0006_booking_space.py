# Generated by Django 3.0 on 2020-06-23 03:45

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_auto_20200617_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('people', models.IntegerField(default=0)),
                ('floor', models.IntegerField(default=0)),
                ('space_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='space_image')),
                ('isavailable', models.BooleanField(default=True)),
                ('isPaidfor', models.BooleanField(default=False)),
                ('dateBooked', models.DateTimeField()),
                ('expiresDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('villager', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('plan', models.CharField(blank=True, choices=[('daily', 'daily'), ('regular', 'regular'), ('vip', 'vip'), ('dedicated standard', 'dedicated standard'), ('dedicted classic', 'dedicated classic'), ('dedicated premium 1', 'dedicated premium 1'), ('dedicated premium 2', 'dedicated premium 2'), ('dedicated premium 3', 'dedicated premium 3'), ('dedicated premium 4', 'dedicated premium 4'), ('dedicated enterprise', 'dedicated enterprise'), ('dedicated single', 'dedicated single'), ('virtual premium', 'virtual premium'), ('virtual lite', 'virtual lite'), ('meeting room 1', 'meeting room 1'), ('meeting room 2', 'meeting room 2'), ('training room', 'training room')], max_length=50, null=True)),
                ('dateBooked', models.DateTimeField(auto_now_add=True)),
                ('expiresDate', models.DateTimeField(blank=True, null=True)),
                ('isavailable', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(default=1)),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.Space')),
            ],
        ),
    ]
