# Generated by Django 2.2.14 on 2020-09-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0013_auto_20200902_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
