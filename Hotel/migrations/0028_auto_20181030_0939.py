# Generated by Django 2.0.7 on 2018-10-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0027_auto_20181023_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomstatus',
            name='ending_Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='roomstatus',
            name='starting_Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='roomstatus',
            name='status_UpdateTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
