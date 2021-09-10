from django.db import models
from django.contrib.auth import get_user_model


AuthUserModel = get_user_model()


class Store(models.Model):
    name = models.CharField(max_length=128, unique=True, null=False)
    # owner_id = models.OneToOneField(AuthUserModel, on_delete=models.SET_NULL)
    owner = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Store object ID = {self.id}>'
