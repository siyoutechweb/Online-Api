# Generated by Django 2.2.14 on 2020-08-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200807_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_store',
            field=models.BooleanField(default=False),
        ),
    ]