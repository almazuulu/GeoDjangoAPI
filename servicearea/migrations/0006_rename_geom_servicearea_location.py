# Generated by Django 4.0.4 on 2022-05-30 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicearea', '0005_remove_servicearea_lat_remove_servicearea_lon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='geom',
            new_name='location',
        ),
    ]
