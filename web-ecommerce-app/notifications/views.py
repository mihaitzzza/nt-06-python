from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from notifications.models import Notification


@login_required
def show_notifications(request):
    notifications = Notification.objects.filter(user=request.user).all()

    # for n in notifications:
    #     print('n.model_class()', n.content_object, type(n.content_object))

    return render(request, 'notifications/view_all.html', {
        'notifications': notifications
    })
