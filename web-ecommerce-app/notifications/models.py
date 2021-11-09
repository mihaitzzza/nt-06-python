from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.shortcuts import reverse


class NotificationTypes(models.TextChoices):
    NEW_STORE = 'new_store'
    NEW_PRODUCT = 'new_product'


class TimestampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Notification(TimestampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    is_seen = models.BooleanField(default=False)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # message = models.CharField(max_length=255, null=True, default=None)
    # link = models.CharField(max_length=255, null=True, default=None)
    type = models.CharField(choices=NotificationTypes.choices, null=True, default=None, max_length=50)

    @property
    def message(self):
        if self.type == NotificationTypes.NEW_STORE.value:
            return f'New awesome store {self.content_object.name} is finally here!'
        elif self.type == NotificationTypes.NEW_PRODUCT.value:
            return f'Product {self.content_object.name} was added to our platform.'

        raise ValueError('Unhandled notification type')

    @property
    def link(self):
        if self.type == NotificationTypes.NEW_STORE.value:
            return reverse('stores:details', args=(self.content_object.id,))
        elif self.type == NotificationTypes.NEW_PRODUCT.value:
            return reverse('products:details', args=(self.content_object.id,))

        raise ValueError('Unhandled notification type')
