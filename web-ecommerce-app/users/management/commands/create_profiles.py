from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

AuthUserModel = get_user_model()


class Command(BaseCommand):
    help = 'Create profiles for users without profile.'

    def handle(self, *args, **options):
        users = AuthUserModel.objects.filter(profile=None)

        print(f'Command will update a total of {len(users)} users.')

        for user in users:
            # profile = Profile(
            #     user=user
            # )
            # profile.save()
            Profile.objects.create(
                user=user
            )
