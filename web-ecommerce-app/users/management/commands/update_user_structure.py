import os
import json
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', dest='fixture_file_path', type=str)

    def handle(self, *args, **options):
        fixture_file_path = options.get('fixture_file_path')
        print('update users fixtures', fixture_file_path)

        if fixture_file_path is None:
            raise CommandError('Fixture file should be provided!')

        if not os.path.isfile(fixture_file_path):
            raise CommandError('File not exists!')

        if not fixture_file_path.endswith('.json'):
            raise CommandError('Not able to parse this type of file.')

        with open(fixture_file_path) as fixture_file:
            users = json.load(fixture_file)

        for user in users:
            user['model'] = 'users.authuser'
            fields = user['fields']

            if 'username' in fields:
                email = fields.get('email')

                if email is None or email == '':
                    fields['email'] = f'{fields["username"]}@gmail.com'

                del fields['username']

        with open(fixture_file_path, 'w') as fixture_file:
            json.dump(users, fixture_file, indent=2)
