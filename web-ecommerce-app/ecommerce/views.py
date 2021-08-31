from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html', {
        'title': 'Django Ecommerce',
        'services': [{
            'name': 'Happy clients',
            'value': '1000+',
        }, {
            'name': 'Available products',
            'value': '2000+'
        }, {
            'name': 'Reviews',
            'value': '4.9/5'
        }]
    })
