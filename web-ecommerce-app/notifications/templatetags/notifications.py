from django import template

register = template.Library()


@register.filter(name='unseen')
def get_user_unseen_notifications(notifications):
    return len(notifications.filter(is_seen=False))