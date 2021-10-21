import json
from users.models.details import Cart as CartModel
from products.models import Product
from payments.models import Order, OrderItem


class Cart:
    def __init__(self, request):
        self._user = request.user
        self._data = request.session['cart'] if 'cart' in request.session else {}
        self._session = request.session

    @property
    def amount(self):
        products = Product.objects.filter(id__in=self._data.keys())
        return self._get_products_total(products)

    def _get_products_total(self, products):
        total = sum([
            float(product.price) * int(self._data[str(product.id)])
            for product in products
        ])

        return total

    def add(self, product_id, quantity):
        product_id_str = str(product_id)

        if product_id_str in self._data:  # { '4': '10' }
            old_quantity = self._data[product_id_str]
            old_quantity = int(old_quantity)

            new_quantity = old_quantity + quantity

            self._data[product_id_str] = str(new_quantity)
        else:
            self._data[product_id_str] = str(quantity)

        self._save()

    def remove(self, product_id):
        del self._data[str(product_id)]
        self._save()

    def _save(self):
        self._session['cart'] = self._data

        if hasattr(self._user, 'cart'):
            self._user.cart.data = json.dumps(self._data)
            self._user.cart.save()
        else:
            CartModel.objects.create(user=self._user, data=json.dumps(self._data))

    def create_order(self):
        order = Order.objects.create(
            user=self._user,
        )

        products = Product.objects.filter(id__in=self._data.keys())
        total = self._get_products_total(products)

        for product in products:
            OrderItem.objects.create(
                order=order,
                product=product,
                price=product.price,
            )

        self._reset()

        return order, total

    def _reset(self):
        self._data = {}
        self._save()
