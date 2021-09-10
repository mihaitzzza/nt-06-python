from django.shortcuts import render
from products.models import Store


def show_stores(request):
    return render(request, 'stores/stores.html', {
        'stores': Store.objects.all(),
    })
