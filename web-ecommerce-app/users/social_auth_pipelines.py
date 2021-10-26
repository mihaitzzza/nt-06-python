import os
import requests
import urllib.request
from uuid import uuid4
from django.core.files.base import ContentFile
from django.core.files import File
from django.conf import settings

USER_FIELDS = ['email', 'first_name', 'last_name']


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    # print('details', details)
    # {'email': <email_address>, 'fullname': <full_name>, 'first_name': <f_name>, 'last_name': <l_name>}

    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))

    print('fields', fields)

    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields, is_social_user=True)
    }


def set_profile_picture(strategy, details, backend, user, is_new, *args, **kwargs):
    if is_new:
        response = kwargs.get('response')

        if response:
            profile_picture_url = None

            if backend.name == 'facebook':
                profile_picture_url = 'https://graph.facebook.com/%s/picture?access_token=%s&type=large' % (
                    response['id'],
                    response['access_token']
                )
            elif backend.name == 'google-oauth2':
                profile_picture_url = response['picture']

            if profile_picture_url:
                try:
                    profile_image_response = requests.get(profile_picture_url)
                except requests.HTTPError:
                    pass
                else:
                    profile = user.profile
                    profile.avatar.save(f'{uuid4()}.jpg', ContentFile(profile_image_response.content))

                # filename = f'{uuid4()}.jpg'
                # try:
                #     urllib.request.urlretrieve(profile_picture_url,
                #                                os.path.join(settings.BASE_DIR, 'media', 'profile_images', filename))
                # except Exception:
                #     pass
                # else:
                #     profile = user.profile
                #     profile.avatar.save(filename, File(open(filename, 'wb')))
