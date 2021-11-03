from django.contrib import admin
from django.utils.html import format_html
from my_admin.admin import my_admin_site
from products.models import Category, Product


@admin.register(Category, site=my_admin_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product, site=my_admin_site)
class ProductAdmin(admin.ModelAdmin):
    def color_html(self, obj):
        if obj.color:
            return format_html(
                f'<div style="width: 20px; height: 20px; border-radius: 50%; background-color: {obj.color}; border: 1px solid black;"></div>'
            )

        return 'N/A'
    color_html.short_description = 'color'
    color_html.admin_order_field = 'color'

    list_display = ('name', 'store_name', 'price', 'color_html', 'size')


# admin.site.register(Category, site=my_admin_site)
# my_admin_site.register(Category, CategoryAdmin)
