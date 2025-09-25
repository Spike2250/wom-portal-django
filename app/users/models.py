from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150, blank=False,
        verbose_name=_("First name"),
    )
    last_name = models.CharField(
        max_length=150, blank=False,
        verbose_name=_("Last name"),
    )
    patronymic = models.CharField(
        max_length=150, blank=True,
        verbose_name=_("Patronymic"),
    )
    email = models.EmailField(
        blank=False,
        verbose_name=_("Email address"),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_fullname(self):
        if self.patronymic:
            return f"{self.last_name} {self.first_name} {self.patronymic}"
        else:
            return f"{self.last_name} {self.first_name}"

    def get_short_name(self):
        if self.patronymic:
            return f"{self.last_name} {self.first_name[0]}.{self.patronymic[0]}."
        else:
            return f"{self.last_name} {self.first_name[0]}."

    def __str__(self):
        return self.username
