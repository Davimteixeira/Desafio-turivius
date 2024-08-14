from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    is_first_login = models.BooleanField(default=True)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Usuários"
