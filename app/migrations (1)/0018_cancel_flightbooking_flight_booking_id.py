# Generated by Django 4.0.2 on 2023-04-19 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_cancel_booking_hotel_bookin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancel_flightbooking',
            name='flight_booking_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.booking', unique=True),
        ),
    ]
