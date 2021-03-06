# Generated by Django 3.1.3 on 2020-11-30 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_auto_20201127_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElecMoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_EMoto', models.CharField(max_length=120)),
                ('Belong_Station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.station')),
            ],
        ),
        migrations.CreateModel(
            name='ElecBike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_EBike', models.CharField(max_length=120)),
                ('Belong_Station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.station')),
            ],
        ),
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Bike', models.CharField(max_length=120)),
                ('Belong_Station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.station')),
            ],
        ),
    ]
