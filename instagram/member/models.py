
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

    # REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ['age']



