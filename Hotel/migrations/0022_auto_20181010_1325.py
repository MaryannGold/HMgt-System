# Generated by Django 2.0.7 on 2018-10-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0021_auto_20181010_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomcategory',
            name='category_descriptions',
            field=models.CharField(max_length=500),
        ),
    ]
