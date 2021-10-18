from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from products.models import Product
from products.forms import FilterProductsForm
from utils.cart import Cart


def show_all_products(request):
    form = FilterProductsForm(data=request.GET)
    products = form.apply_filters()

    paginator = Paginator(products, 4)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request, 'products/products.html', {
        'page_obj': page_obj,
        'form': form,
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


def show_checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = [
        {
            "product": product,
            "quantity": cart[str(product.id)],
            "total": '%.2f' % (float(product.price) * int(cart[str(product.id)]))
        }
        for product in products
    ]

    return render(request, 'products/checkout.html', {
        'cart_items': cart_items,
        'cart': cart
    })


def remove_product_from_cart(request, product_id):
    get_object_or_404(Product, pk=product_id)

    cart = Cart(request)
    cart.remove(product_id)

    return redirect(reverse('products:checkout'))
