# Generated by Django 2.2.14 on 2020-08-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='store',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
