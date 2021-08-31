from django.urls import path
from products.views import show_all_products, show_product_details

app_name = 'products'

urlpatterns = [
    path('', show_all_products, name='all'),  # this is already localhost:8000/products/
    path('<int:product_id>/', show_product_details, name='details'),
]
