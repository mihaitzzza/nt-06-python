from django.db import models
from django.contrib.auth import get_user_model


AuthUserModel = get_user_model()


class Store(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    # owner_id = models.OneToOneField(AuthUserModel, on_delete=models.SET_NULL)
    owner = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)

    def user_email(self):
        return self.owner.email
    user_email.short_description = 'owner email'
    user_email.admin_order_field = 'owner__email'

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Store object ID = {self.id}>'
