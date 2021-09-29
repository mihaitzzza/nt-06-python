from django.db import models
from django.contrib.auth import get_user_model
from django.templatetags.static import static

AuthUserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default=None)

    @property
    def image(self):
        print('*' * 100)
        print('self.avatar', self.avatar)

        if self.avatar:
            print('self.avatar.url', self.avatar.url)
            return self.avatar.url

        return static('images/defaultUser.jpg')

