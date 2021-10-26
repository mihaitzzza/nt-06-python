import secrets
from django.shortcuts import render, Http404, reverse, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from users.forms import RegisterForm, ProfileImageForm, PasswordForm
from users.models import Activation
from users.email import send_activation_mail
from utils.constants.activation import ACTIVATION_DICT


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next', None)

        # if not username or not password:
        #     raise Http404('Username or password not provided!')
        user = authenticate(request, username=username, password=password)

        if user is None:
            raise Http404('Username or password not provided!')
        else:
            login(request, user)

            if next:
                return redirect(next)

            return redirect('/')

    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
    else:
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')

    return render(request, 'users/register.html', {
        'form': form,
    })


@login_required
def show_profile(request):
    # if request.method == 'GET':
    #     form = ProfileImageForm()
    # else:
    #     form = ProfileImageForm(request.POST, request.FILES)
    #
    #     if form.is_valid():
    #         form.save()
    #
    #         return redirect(reverse('users:profile'))
    if request.method == 'GET':
        form = ProfileImageForm()
    else:
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form
    })


def activate(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.expires_at < timezone.now():
        return redirect(reverse('users:regenerate_token', args=(token,)))

    if request.method == 'GET':
        form = PasswordForm(activation.user)
    else:
        form = PasswordForm(activation.user, request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('users:login'))

    return render(request, 'users/set_password.html', {
        'form': form,
        'token': token,
    })


def regenerate_token(request, token):
    activation = get_object_or_404(Activation, token=token)

    if activation.expires_at >= timezone.now():
        return redirect('users:activate', args=(token,))

    activation.token = secrets.token_hex(32)
    activation.expires_at = timezone.now() + timezone.timedelta(**ACTIVATION_DICT)
    activation.save()

    send_activation_mail(activation)

    return redirect('/')
