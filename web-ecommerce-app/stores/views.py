from django.shortcuts import render, get_object_or_404
from products.models import Store


def show_stores(request):
    return render(request, 'stores/stores.html', {
        'stores': Store.objects.all(),
    })


def show_details(request, id):
    store = get_object_or_404(Store, pk=id)

    return render(request, 'stores/details.html', {
        'store': store
    })
