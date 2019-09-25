# Generated by Django 2.2.4 on 2019-09-20 18:09

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xiaomi', '0021_auto_20190920_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='xiaomi',
            name='real_dolar',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15),
        ),
    ]