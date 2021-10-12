from django import template

register = template.Library()


# @register.filter(name='products_no')
# def get_cart_products_number(session):
#     cart = session.get('cart', {})
#     return len(cart.keys())


@register.filter(name='dict_length')
def dict_length(parent, key):
    my_dict = parent.get(key, {})
    return len(my_dict.keys())
