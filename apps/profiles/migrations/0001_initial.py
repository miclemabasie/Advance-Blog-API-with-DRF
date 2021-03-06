# Generated by Django 3.2.7 on 2022-06-24 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('about_me', models.TextField(verbose_name='Say something about yourself...')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+237670181442', max_length=30, region=None, verbose_name='Phone Number')),
                ('profile_photo', models.ImageField(default='profile_defualt.png', upload_to='', verbose_name='Profile Photo')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Other', max_length=100, verbose_name='Gender')),
                ('proffessional', models.CharField(max_length=100, verbose_name='What do you do for a living')),
                ('country', django_countries.fields.CountryField(blank=True, default='CM', max_length=100, null=True, verbose_name='Country')),
                ('city', models.CharField(blank=True, default='Bamenda', max_length=100, null=True, verbose_name='City')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
