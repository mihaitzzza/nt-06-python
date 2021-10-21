from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

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


class Order(models.Model):
    user = models.ForeignKey(AuthUserModel, on_delete=models.SET_NULL, null=True, default=None, related_name='orders')

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
