# Generated by Django 3.2.6 on 2021-10-13 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211013_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_column', models.IntegerField(default=None, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_pivot', to='products.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories_pivot', to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='products.ProductCategory', to='products.Category'),
        ),
    ]