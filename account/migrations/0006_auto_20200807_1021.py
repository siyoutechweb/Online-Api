# Generated by Django 2.2.14 on 2020-08-07 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_profile_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='store',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shopApp.Store'),
        ),
    ]
