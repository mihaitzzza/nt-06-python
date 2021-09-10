from django.db import models
from django.contrib.auth import get_user_model
from utils import XS, S, M, L, XL, XXL
from utils.constants.size import SIZES
from stores.models import Store

AuthUserModel = get_user_model()


class Product(models.Model):
    name = models.CharField(max_length=128, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products', default=None, null=True)
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # max => 999.99
    color = models.CharField(max_length=10, null=False)
    size = models.IntegerField(choices=((XS, 'XS'), (S, 'S'), (M, 'M'), (L, 'L'), (XL, 'XL'), (XXL, 'XXL')))
    gender = models.CharField(choices=(('M', 'male'), ('F', 'female')), max_length=1)

    @property
    def human_size(self):
        return SIZES.get(self.size, None)

    def __str__(self):
        return f'<Product object ID = {self.id}>'
