from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_fullname()
