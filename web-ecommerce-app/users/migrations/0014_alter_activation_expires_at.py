# Generated by Django 3.2.6 on 2021-11-10 16:41

from django.db import migrations, models
import users.models.details


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_activation_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=users.models.details.expires_at_time),
        ),
    ]
