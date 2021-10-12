from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from products.models import Product
from utils.cart import Cart


def show_all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 4)

    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request, 'products/products.html', {
        'page_obj': page_obj,
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


def add_product_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(product_id, quantity)

    return redirect(reverse('products:all'))
