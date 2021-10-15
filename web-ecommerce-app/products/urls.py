from django.urls import path
from products.views import show_all_products, show_product_details, add_product_to_cart, show_checkout, remove_product_from_cart

app_name = 'products'

urlpatterns = [
    path('', show_all_products, name='all'),  # this is already localhost:8000/products/
    path('<int:product_id>/', show_product_details, name='details'),
    path('<int:product_id>/add_to_cart', add_product_to_cart, name='add_to_cart'),  # localhost:8000/products/<p_id>/add_to_cart
    path('checkout/', show_checkout, name='checkout'),
    path('<int:product_id>/remove_from_cart/', remove_product_from_cart, name='remove_from_cart'),
]
