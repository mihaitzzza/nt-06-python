from django.contrib import admin
from my_admin.admin import my_admin_site
from stores.models import Store


@admin.register(Store, site=my_admin_site)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_email')
    ordering = ('owner__email',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            return queryset

        return queryset.filter(owner=request.user)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)

        if not request.user.is_superuser:
            fields.remove('owner')

        return fields

    def save_model(self, request, obj, form, change):
        if not obj.pk and not request.user.is_superuser:
            obj.owner = request.user

        return super().save_model(request, obj, form, change)

