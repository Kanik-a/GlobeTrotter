# Generated by Django 4.0.2 on 2023-04-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_hotel_details_total_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_details',
            name='total_room',
            field=models.IntegerField(default=0, verbose_name=6000),
            preserve_default=False,
        ),
    ]
