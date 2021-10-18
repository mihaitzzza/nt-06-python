from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from payments.utils import create_stripe_customer_model

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_stripe_customer(created, instance, **kwargs):
    if created:
        create_stripe_customer_model(instance)
