from django.contrib.auth import get_user_model
from notifications.models import Notification

AuthUserModel = get_user_model()


def create_notification(obj, message, link):
    if not obj or not message or not link:
        raise ValueError('Required data not provided.')

    users = AuthUserModel.objects.filter(is_staff=False).all()

    for user in users:
        Notification.objects.create(
            user=user,
            content_object=obj,
            message=message,
            link=link
        )
