# Generated by Django 3.2.6 on 2021-11-10 16:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_activation_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 10, 17, 9, 39, 201639, tzinfo=utc)),
        ),
    ]
