
from django.contrib.auth.models import (
    AbstractUser,
    UserManager as DjangoUserManager
)

from django.db import models


class UserManager(DjangoUserManager):
    def create_user(self, email, *args, **kwargs):
        super().create_superuser(age="30", *args, **kwargs)

class User(AbstractUser):
    img_profile = models.ImageField(
        upload_to='user',
        blank=True)
    age = models.IntegerField()

    #like_posts = MTM으로 연결

    objects = UserManager()

    # def like_post(self, post):
    # 자신의 like_posts에 해당 내용 추가



