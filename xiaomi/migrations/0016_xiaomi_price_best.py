# Generated by Django 2.2.4 on 2019-09-16 22:39

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaomi', '0015_auto_20190916_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiaomi',
            name='price_best',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15),
        ),
    ]