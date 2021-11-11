import os
import stripe
import xlsxwriter
from django.conf import settings
from django.utils import timezone
from payments.models import StripeCustomer


def create_stripe_customer_model(user_instance):
    stripe_customer = stripe.Customer.create(
        email=user_instance.email,
        name=f'{user_instance.first_name} {user_instance.last_name}',
        api_key=settings.STRIPE_SECRET_KEY
    )

    StripeCustomer.objects.create(user=user_instance, stripe_id=stripe_customer['id'])


def get_user_payment_methods_details(user):
    # # Using Stripe PaymentMethod resource
    # payment_methods_response = stripe.PaymentMethod.list(
    #     customer=user.stripe_customer.stripe_id,
    #     type='card',
    #     api_key=settings.STRIPE_SECRET_KEY,
    # )
    #
    # cards = [data['card'] for data in payment_methods_response['data']]

    # # Using Stripe Cards resource
    # cards_response = stripe.Customer.list_sources(
    #     user.stripe_customer.stripe_id,
    #     object="card",
    #     api_key=settings.STRIPE_SECRET_KEY,
    # )
    #
    # return cards_response['data']

    print('user.stripe_customer.cards', user.stripe_customer.cards)

    return user.stripe_customer.cards.all()


def generate_xlsx_report(orders):
    first_column = 65
    report_header = [
        'PRODUCT',
        'PRICE',
        'QUANTITY',
        'TOTAL'
    ]

    current_date = timezone.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'{current_date}.xlsx'
    file_dir = os.path.join(settings.MEDIA_ROOT, 'reports')
    file_path = os.path.join(file_dir, file_name)
    os.makedirs(file_dir, exist_ok=True)

    workbook = xlsxwriter.Workbook(file_path)
    for order in orders:
        worksheet = workbook.add_worksheet(f'Order {order["id"]}')

        for index, header in enumerate(report_header):
            column_index = chr(first_column + index)  # A, B, C ...
            worksheet.write(f'{column_index}1', header)

        for p_index, product in enumerate(order['products']):
            product_info = product.values()
            total_index = len(product_info)
            product_row_index = p_index + 2

            for i_index, info in enumerate(product_info):
                column_index = chr(first_column + i_index)  # A, B, C ...
                if type(info) == float:
                    worksheet.write_number(f'{column_index}{product_row_index}', info)
                else:
                    worksheet.write(f'{column_index}{product_row_index}', info)

            total_column = chr(first_column + total_index)
            total_cell_index = f'{total_column}{product_row_index}'

            price_column_index = chr(first_column + 1)
            price_cell_index = f'{price_column_index}{product_row_index}'

            quantity_column_index = chr(first_column + 2)
            quantity_cell_index = f'{quantity_column_index}{product_row_index}'

            worksheet.write_formula(total_cell_index, f'={price_cell_index}*{quantity_cell_index}')

    workbook.close()

    return file_path
