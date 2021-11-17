# Generated by Django 3.2.6 on 2021-11-10 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-11-10 18:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]