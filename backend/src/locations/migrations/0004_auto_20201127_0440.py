# Generated by Django 3.1.3 on 2020-11-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20201127_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent_detail',
            name='timeArrive',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='rent_detail',
            name='timeDepart',
            field=models.TimeField(),
        ),
    ]
