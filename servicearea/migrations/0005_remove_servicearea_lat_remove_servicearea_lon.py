# Generated by Django 4.0.4 on 2022-05-30 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicearea', '0004_remove_servicearea_poly_servicearea_geom_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicearea',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='servicearea',
            name='lon',
        ),
    ]
