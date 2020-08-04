# Generated by Django 3.0.8 on 2020-08-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pp_id', models.IntegerField()),
                ('planname', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
                ('planformula', models.CharField(max_length=45)),
                ('location', models.CharField(max_length=45)),
                ('planstatus', models.CharField(max_length=1)),
                ('createdate', models.DateField()),
                ('updatedate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PricingPlanOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppo_id', models.IntegerField()),
                ('planid', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('status', models.CharField(max_length=1)),
                ('createdate', models.DateField()),
                ('updatedate', models.DateField()),
            ],
        ),
    ]
