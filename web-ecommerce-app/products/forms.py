from django import forms
from products.models import Category, Product

ORDER_BY_CHOICES = (('POPULARITY', 'Popularity'), ('PRICE_ASC', 'Price ascending'), ('PRICE_DESC', 'Price descending'))


def get_orderby_field(order_by):
    if order_by == 'PRICE_ASC':
        return 'price'

    if order_by == 'PRICE_DESC':
        return '-price'

    return 'id'


class FilterProductsForm(forms.Form):
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES)
    categories = forms.ChoiceField(choices=(), widget=forms.CheckboxSelectMultiple)
    min_price = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    max_price = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        self.fields['categories'].choices = tuple((category.id, category.name) for category in categories)

    # def clean_order_by(self):
    #     print('--------------- self.cleaned_data', self.cleaned_data)
    #     return 'PRICE_ASC'
    #
    # def clean_categories(self):
    #     print('--------------- self.cleaned_data', self.cleaned_data)
    #     return [1, 2]

    def apply_filters(self):
        is_valid = self.is_valid()
        print('is_valid', is_valid)
        if is_valid:
            print('++++ self.cleaned_data', self.cleaned_data)
            order_by = get_orderby_field(self.cleaned_data.get('order_by'))
            categories = self.cleaned_data.get('categories', [])
            min_price = self.cleaned_data.get('min_price')
            max_price = self.cleaned_data.get('max_price')

            print('categories', categories)
            print('min_price', min_price)
            print('max_price', max_price)

            products = Product.objects.order_by(order_by)
            return products

        raise forms.ValidationError('Not a valid form')
