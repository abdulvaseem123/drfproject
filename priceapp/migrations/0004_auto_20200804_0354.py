# Generated by Django 3.0.8 on 2020-08-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0003_auto_20200804_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricingplan',
            name='createdate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pricingplan',
            name='updatedate',
            field=models.DateField(auto_now=True),
        ),
    ]
