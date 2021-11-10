from django.db import models
from django.conf import settings
from django.templatetags.static import static
from django.utils import timezone
from utils.constants.activation import ACTIVATION_DICT


def expires_at_time():
    return timezone.now() + timezone.timedelta(**ACTIVATION_DICT)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default=None)

    @property
    def image(self):
        if self.avatar:
            return self.avatar.url

        return static('images/defaultUser.jpg')


class Activation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activation')
    token = models.CharField(max_length=64, null=True, default=None, blank=False, unique=True)
    expires_at = models.DateTimeField(default=expires_at_time)
    activated_at = models.DateTimeField(null=True, default=None, blank=False)

    def __str__(self):
        return self.token

    def __repr__(self):
        return self.token


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')  # user.cart
    data = models.JSONField()
