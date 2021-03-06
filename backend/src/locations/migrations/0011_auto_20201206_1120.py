# Generated by Django 3.1.3 on 2020-12-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_auto_20201205_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name_User',
        ),
        migrations.AddField(
            model_name='user',
            name='cmnd',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='Votre email', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='Votre nom', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Votre prenom', max_length=120),
        ),
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='pointReward',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='Votre username', max_length=120),
        ),
    ]
