from django.shortcuts import render, get_object_or_404
from products.models import Product


def show_all_products(request):
    products = Product.objects.all()

    return render(request, 'products/products.html', {
        'products': products,
    })


def show_product_details(request, product_id):
    # products = Product.objects.filter(id=product_id)
    # if len(products) == 0:
    #     raise Http404(f'Product with ID = {product_id} does not exists!')

    # try:
    #     product = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404(f'Product with ID = {product_id} does not exists!')
    # else:
    #     return render(request, 'products/details.html', {
    #         'product': product
    #     })

    # product = get_object_or_404(Product, id=product_id)
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/details.html', {
        'product': product,
    })
