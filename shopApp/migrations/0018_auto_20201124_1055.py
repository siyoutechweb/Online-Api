# Generated by Django 2.2 on 2020-11-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0017_auto_20201121_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_cn',
            field=models.CharField(db_index=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='category',
            name='name_fr',
            field=models.CharField(db_index=True, default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='category',
            name='name_it',
            field=models.CharField(db_index=True, default=None, max_length=200),
        ),
    ]