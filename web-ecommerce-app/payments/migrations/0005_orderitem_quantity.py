# Generated by Django 3.2.6 on 2021-10-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
