# Generated by Django 4.0.6 on 2022-07-18 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_hotelimages_images_hotel_image_one_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HotelImages',
        ),
    ]
