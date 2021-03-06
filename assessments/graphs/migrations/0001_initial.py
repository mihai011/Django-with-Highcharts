# Generated by Django 3.1 on 2020-08-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('sales', models.PositiveIntegerField()),
                ('resale_value', models.PositiveIntegerField()),
                ('vehicle_type', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('engine_size', models.FloatField()),
                ('horsepower', models.SmallIntegerField()),
                ('wheelbase', models.FloatField()),
                ('width', models.FloatField()),
                ('length', models.FloatField()),
                ('curb_weight', models.FloatField()),
                ('fuel_capacity', models.FloatField()),
                ('fuel_efficiency', models.SmallIntegerField()),
                ('latest_launch', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CVSSProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('nr_total_vuln', models.IntegerField(default=0)),
                ('nr_total', models.IntegerField(default=0)),
                ('weighted_average', models.FloatField(default=0)),
                ('percentage_total', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CVSSVendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=100)),
                ('nr_total_vuln', models.IntegerField()),
                ('nr_total', models.IntegerField()),
                ('weighted_average', models.FloatField()),
                ('percentage_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductTop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('vendor', models.CharField(default='Google', max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('nr_total_vuln', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VendorTop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=100)),
                ('nr_products', models.IntegerField()),
                ('nr_total_vuln', models.IntegerField()),
                ('ratio', models.SmallIntegerField()),
            ],
        ),
    ]
