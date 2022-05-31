# Generated by Django 4.0.4 on 2022-05-30 19:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicearea', '0003_alter_servicearea_poly'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicearea',
            name='poly',
        ),
        migrations.AddField(
            model_name='servicearea',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='lon',
            field=models.FloatField(null=True, verbose_name='Longitude'),
        ),
    ]