# Generated by Django 2.2.4 on 2019-09-16 16:29

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaomi', '0007_auto_20190916_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xiaomi',
            name='pricebg',
            field=models.DecimalField(decimal_places=2, default=Decimal('10.000'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='pricedx',
            field=models.DecimalField(decimal_places=2, default=Decimal('10.000'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='pricegb',
            field=models.DecimalField(decimal_places=2, default=Decimal('10.000'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='pricein',
            field=models.DecimalField(decimal_places=2, default=Decimal('10.000'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='pricemz',
            field=models.DecimalField(decimal_places=2, default=Decimal('10.000'), max_digits=10),
        ),
    ]
