from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import format_html
from my_admin.admin import my_admin_site
from products.models import Category, Product, ProductCategory
from stores.models import Store
from notifications.utils import create_notification


@admin.register(Category, site=my_admin_site)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductCategoryTabularInline(admin.TabularInline):
    model = ProductCategory
    extra = 1


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

    def get_categories(self, obj):
        product_categories = obj.categories.order_by('id').all()

        if len(product_categories) > 0:
            return ', '.join([category.name for category in product_categories])

        return 'N/A'
    get_categories.short_description = 'categories'

    list_display = ('name', 'store_name', 'price', 'color_html', 'size', 'get_categories')
    search_fields = ('name', 'color', 'store__name', 'categories__name')
    ordering = ('store__name', 'price', 'color')
    inlines = (ProductCategoryTabularInline,)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'store' and not request.user.is_superuser:
            kwargs['queryset'] = Store.objects.filter(owner=request.user)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        message = f'Product {obj.name} was added to our platform.'
        link = reverse('products:details', args=(obj.id,))
        create_notification(obj, message, link)


# admin.site.register(Category, site=my_admin_site)
# my_admin_site.register(Category, CategoryAdmin)
