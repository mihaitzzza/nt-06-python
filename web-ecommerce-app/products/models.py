from django.db import models
from django.contrib.auth import get_user_model
from utils import XS, S, M, L, XL, XXL
from utils.constants.size import SIZES
from stores.models import Store

AuthUserModel = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('-id',)

    name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return '<Category ID=%s | name="%s"' % (self.id, self.name)


class Product(models.Model):
    name = models.CharField(max_length=128, null=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='products', default=None, null=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, default=None)
    # category = models.ManyToManyField(Category, related_name='products')
    categories = models.ManyToManyField(Category, through='ProductCategory', related_name='products')
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # max => 999.99
    color = models.CharField(max_length=10, null=False)
    size = models.IntegerField(choices=((XS, 'XS'), (S, 'S'), (M, 'M'), (L, 'L'), (XL, 'XL'), (XXL, 'XXL')))
    gender = models.CharField(choices=(('M', 'male'), ('F', 'female')), max_length=1)

    @property
    def human_size(self):
        return SIZES.get(self.size, None)

    def store_name(self):
        if hasattr(self.store, 'name'):
            return self.store.name

        return '-'
    store_name.short_description = 'shop name'
    store_name.admin_order_field = 'store__name'

    def __str__(self):
        return f'<Product object ID = {self.id}>'


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='categories_pivot')  # product.categories[0].category.name
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products_pivot')  # category.products[0].product.name
    extra_column = models.IntegerField(null=True, default=None)
