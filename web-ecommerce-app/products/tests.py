from parameterized import parameterized
from random import randrange
from django.test import TestCase
from django.shortcuts import reverse
from products.models import Product


class ProductsTestCase(TestCase):
    def setUp(self) -> None:
        for i in range(1000):
            Product.objects.create(
                name=f'Product #{i + 1}',
                quantity=randrange(25, 75),
                price=randrange(50, 999),
                size=2,
            )

    def test_products_page_pagination(self):
        for page_index in range(0, 250):
            response = self.client.get(reverse('products:all'), {
                'page': page_index + 1
            })
            page = response.context['page_obj']
            paginator = page.paginator
            self.assertEqual(paginator.num_pages, 250)

            result_products = response.context['page_obj'].object_list

            # i:0 => 0, 4
            # i:1 => 4, 8
            slice_start = page_index * 4
            slice_end = (page_index + 1) * 4
            expected_products = Product.objects.all()[slice_start:slice_end]

            self.assertEqual(len(result_products), 4)
            self.assertQuerysetEqual(expected_products, result_products)

    @parameterized.expand((
        ('order_by', 'PRICE_ASC'),
        ('order_by', 'PRICE_DESC'),
    ))
    def test_products_page_pagination_filters(self, order_filter_name, order_filter_value):
        for page_index in range(0, 250):
            response = self.client.get(reverse('products:all'), {
                order_filter_name: order_filter_value,
                'page': page_index + 1
            })

            result_products = response.context['page_obj'].object_list
            slice_start = page_index * 4
            slice_end = (page_index + 1) * 4
            order_by = 'price' if order_filter_value == 'PRICE_ASC' else '-price'
            expected_products = Product.objects.order_by(order_by).all()[slice_start:slice_end]

            self.assertQuerysetEqual(expected_products, result_products)
