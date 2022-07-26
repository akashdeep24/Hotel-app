# Generated by Django 4.0.6 on 2022-07-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelimages',
            name='images',
        ),
        migrations.AddField(
            model_name='hotel',
            name='image_one',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='image_three',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='image_two',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
        migrations.AddField(
            model_name='hotelimages',
            name='images_one',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
        migrations.AddField(
            model_name='hotelimages',
            name='images_three',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
        migrations.AddField(
            model_name='hotelimages',
            name='images_two',
            field=models.ImageField(default='', upload_to='home/images'),
        ),
    ]
