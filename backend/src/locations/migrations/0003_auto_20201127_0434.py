# Generated by Django 3.1.3 on 2020-11-26 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_rent_detail_station_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent_detail',
            name='stationArrive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentdetail_stationDepart', to='locations.station'),
        ),
        migrations.AlterField(
            model_name='rent_detail',
            name='stationDepart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentdetail_stationArrive', to='locations.station'),
        ),
    ]
