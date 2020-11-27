# Generated by Django 2.2 on 2020-10-21 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0014_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopApp.Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopApp.Category'),
        ),
    ]
