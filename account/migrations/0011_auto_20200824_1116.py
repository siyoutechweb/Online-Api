# Generated by Django 2.2.14 on 2020-08-24 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200821_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='No address configured yet', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='No city configured yet', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(default='No country configured yet', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='No phone number configured yet', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='street',
            field=models.CharField(default='No street configured yet', max_length=200),
        ),
        migrations.AddField(
            model_name='profile',
            name='zip_code',
            field=models.IntegerField(default='1234'),
        ),
    ]
