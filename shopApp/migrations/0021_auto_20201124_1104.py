# Generated by Django 2.2 on 2020-11-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0020_auto_20201124_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='parentcategory',
            name='name_cn',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='name_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='parentcategory',
            name='name_it',
            field=models.CharField(max_length=200, null=True),
        ),
    ]