
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
        '프로필 이미지',
        upload_to='user',
        blank=True)
    age = models.IntegerField('나이')

    like_post = models.ManyToManyField(
        'post.Post',
        verbose_name='좋아요 누른 포스트 목록'
    )

    objects = UserManager()

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = f'{verbose_name} 목록'

    # def like_post(self, post):
    # 자신의 like_posts에 해당 내용 추가


