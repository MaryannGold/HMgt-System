# Generated by Django 2.0.7 on 2018-08-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0003_auto_20180831_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_image',
            field=models.ImageField(upload_to='website/media/hotel_images/'),
        ),
    ]
