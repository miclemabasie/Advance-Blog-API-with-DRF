# Generated by Django 3.2.7 on 2022-06-24 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='profile_default.png', upload_to='', verbose_name='Profile Photo'),
        ),
    ]
