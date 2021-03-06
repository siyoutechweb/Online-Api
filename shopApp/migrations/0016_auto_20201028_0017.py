# Generated by Django 2.2 on 2020-10-27 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0015_auto_20201021_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(default='123456789', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopApp.Brand'),
        ),
    ]
