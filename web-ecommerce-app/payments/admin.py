from django.contrib import admin
from payments.models import Order
from my_admin.admin import my_admin_site
from payments.utils import generate_xlsx_report
from payments.models import Report
from django.shortcuts import redirect


class PriceFilter(admin.SimpleListFilter):
    title = 'price'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('<100', 'max. 100 RON'),
            ('100-500', '100 - 500 RON'),
            ('>500', 'min. 500 RON')
        )

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset

        def filter_by_price(order_price):
            if self.value() == '<100':
                return float(order_price) < 100

            if self.value() == '100-500':
                return 100 <= float(order_price) <= 500

            return float(order_price) > 500

        filtered_orders = [
            order.id for order in queryset if filter_by_price(order.amount)
        ]

        return queryset.filter(id__in=filtered_orders)
        # return queryset.filter(price__lt=self.value())
        # return queryset.filter(price__lte=self.value(), price__gte=self.value())
        # return queryset.filter(price__gt=self.value())


@admin.register(Order, site=my_admin_site)
class OrderAdmin(admin.ModelAdmin):
    @admin.action(description='Generate XLSX report')
    def generate_report(self, request, queryset):
        report_orders = [
            {
                "id": order.id,
                "number": order.number,
                "date": order.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "products": [
                    {
                        "name": order_item.product.name,
                        "price": float(order_item.price),
                        "quantity": order_item.quantity,
                    }
                    for order_item in order.items.all()
                ]
            }
            for order in queryset
        ]

        media_path = generate_xlsx_report(report_orders)

        report = Report(user=request.user)
        report.file.name = media_path
        report.save()

        return redirect(f'/admin/payments/report/{report.id}/change/')

    list_display = ('number', 'currency_amount', 'human_date')
    list_filter = ('created_at', PriceFilter)
    actions = (generate_report,)


@admin.register(Report, site=my_admin_site)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'file')
