from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from ecommerce.models import TimestampModel

AuthUserModel = get_user_model()


class StripeCustomer(models.Model):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='stripe_customer')
    stripe_id = models.CharField(max_length=255, default=None, null=True)


class StripeCard(models.Model):
    stripe_customer = models.ForeignKey(StripeCustomer, on_delete=models.CASCADE, related_name='cards')
    stripe_id = models.CharField(max_length=255, default=None, null=True)
    last4 = models.CharField(max_length=4, default=None, null=True)
    exp_month = models.IntegerField(default=None, null=True)
    exp_year = models.IntegerField(default=None, null=True)

    @property
    def number(self):
        # return '**** **** **** ' + str(self.last4)
        return '**** ' * 3 + str(self.last4)


class Order(TimestampModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.SET_NULL, null=True, default=None, related_name='orders')
    number = models.CharField(max_length=50, null=True, default=uuid4)

    def human_date(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M:%S')
    human_date.short_description = 'date'
    human_date.admin_order_field = 'created_at'

    def currency_amount(self):
        return f'{self.amount} RON'
    currency_amount.short_description = 'Price'

    @property
    def amount(self):
        total = sum([
            float(item.price) * item.quantity
            for item in self.items.all()
        ])

        return '%.2f' % total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, default=None, related_name='product')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def product_name(self):
        if self.product is None:
            return 'Unknown'

        return self.product.name
