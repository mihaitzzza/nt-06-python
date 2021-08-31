from django.shortcuts import render, HttpResponse, Http404

products = [{
    'id': 1,
    'name': 'Product #1',
    'price': 20.50
}, {
    'id': 2,
    'name': 'Product #2',
    'price': 20.00
}, {
    'id': 3,
    'name': 'Product #3',
    'price': 5.90
}]


def show_all_products(request):
    return render(request, 'products/products.html', {
        'products': products,
    })


def show_product_details(request, product_id):
    founded_products = [p for p in products if p['id'] == product_id]

    if len(founded_products) == 0:
        raise Http404(f'Product with ID = {product_id} does not exists!')

    return render(request, 'products/details.html', {
        'product': founded_products[0]
    })
