# Generated by Django 3.2.6 on 2021-10-18 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(default=None, max_length=255, null=True)),
                ('stripe_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='payments.stripecustomer')),
            ],
        ),
    ]