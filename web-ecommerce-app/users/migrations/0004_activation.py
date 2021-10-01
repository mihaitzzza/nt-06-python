# Generated by Django 3.2.6 on 2021-09-30 17:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_authuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=None, max_length=64, null=True)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2021, 9, 30, 18, 3, 20, 334854, tzinfo=utc))),
                ('activated_at', models.DateTimeField(default=None, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
