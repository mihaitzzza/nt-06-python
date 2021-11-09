from django.contrib.auth import get_user_model
from notifications.models import Notification

AuthUserModel = get_user_model()


def create_notification(obj, type):
    if not obj:
        raise ValueError('Required data not provided.')

    users = AuthUserModel.objects.filter(is_staff=False).all()

    for user in users:
        Notification.objects.create(
            user=user,
            content_object=obj,
            type=type,
        )
