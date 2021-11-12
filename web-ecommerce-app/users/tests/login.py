from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

AuthUserModel = get_user_model()


class LoginTestCase(TestCase):
    def setUp(self) -> None:
        email = 'a@gmail.com'

        user = AuthUserModel.objects.create_user(
            email=email,
            first_name='Mihai',
            last_name='Vladu',
        )
        user.is_active = True
        user.set_password('python123')
        user.save()

        self._user = AuthUserModel.objects.get(email=email)

    def test_user_can_authenticate(self):
        is_authenticated = self.client.login(username=self._user.email, password='python123')
        self.assertEqual(is_authenticated, True)

    def test_login_redirects_to_homepage(self):
        response = self.client.post(reverse('users:login'), {
            'username': self._user.email,
            'password': 'python123',
        })

        self.assertRedirects(response, '/', status_code=302, target_status_code=200)

    def test_login_redirects_to_next_url(self):
        response = self.client.post(reverse('users:login'), {
            'username': self._user.email,
            'password': 'python123',
            'next': reverse('users:profile'),
        })

        self.assertRedirects(response, reverse('users:profile'), status_code=302, target_status_code=200)

    def test_authenticated_user_is_redirected(self):
        # Authenticate user
        self.client.post(reverse('users:login'), {
            'username': self._user.email,
            'password': 'python123',
        })

        # Try to re-login (although user is authenticated)
        response = self.client.post(reverse('users:login'), {
            'username': self._user.email,
            'password': 'python123',
        })

        self.assertRedirects(response, '/', status_code=302, target_status_code=200)
