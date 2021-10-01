from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class AuthUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name):
        user = self.create_user(email, first_name, last_name)

        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user


class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), null=False, blank=False, unique=True)
    password = models.CharField(_('password'), max_length=128, null=True, blank=False, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.email
