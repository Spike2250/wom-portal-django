import uuid

from django.db import models
from django.utils.translation import gettext as _

from ..users.models import User
from ..middleware import get_current_user


class Workplace(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    creator = models.ForeignKey(
        User, blank=False, default=get_current_user, on_delete=models.PROTECT,
    )
    name = models.CharField(
        max_length=255, unique=True, blank=False,
        verbose_name=_('Name'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
