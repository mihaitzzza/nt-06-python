from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
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


@login_required
def mark_as_seen(request, id):
    if request.method == 'POST':
        notification = get_object_or_404(Notification, pk=id)

        if notification.user.id != request.user.id and notification.is_seen:
            return Http404('Not found!')

        notification.is_seen = True
        notification.save()

        return redirect(reverse('notifications:view_all'))

    return Http404('Method not allowed!')
