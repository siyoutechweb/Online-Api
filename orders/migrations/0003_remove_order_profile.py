# Generated by Django 2.2.14 on 2020-08-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='profile',
        ),
    ]