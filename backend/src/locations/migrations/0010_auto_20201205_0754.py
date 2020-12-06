# Generated by Django 3.1.3 on 2020-12-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_auto_20201204_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='history',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='pointReward',
            field=models.CharField(default='0', max_length=120),
        ),
        migrations.AlterField(
            model_name='user',
            name='name_User',
            field=models.CharField(default='Votre nom', max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='Votre username', max_length=120, unique=True),
        ),
    ]