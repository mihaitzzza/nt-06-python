import os
from django.conf import settings


def handle_uploaded_file(file):
    # name_and_extension = file.name.split('.')  # my-file.png => ['my-file', 'png']
    # name = name_and_extension[0]
    # extension = name_and_extension[1]
    # name, extension = tuple(file.name.split('.'))

    destination_dir = os.path.join(settings.MEDIA_ROOT, 'profile_images')
    os.makedirs(destination_dir, exist_ok=True)

    with open(os.path.join(destination_dir, file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
