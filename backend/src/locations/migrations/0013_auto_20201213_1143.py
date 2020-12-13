# Generated by Django 3.1.3 on 2020-12-13 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0012_auto_20201211_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='Available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='elecbike',
            name='Available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='elecmoto',
            name='Available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='stationDepart',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='transportLouer',
            field=models.CharField(default='', max_length=120),
        ),
    ]
