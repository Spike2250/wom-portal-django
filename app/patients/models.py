import uuid

from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField


class Patient(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    fullname = models.CharField(
        max_length=255, blank=False,
        verbose_name=_("Patient fullname"),
    )
    birthdate = models.DateField(
        null=False, blank=False,
        verbose_name=_("Patient birthdate"),
    )
    phone = PhoneNumberField(
        null=False, blank=False, unique=True,
        verbose_name=_("Patient phone number"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
