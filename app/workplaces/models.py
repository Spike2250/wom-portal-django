import uuid

from django.db import models
from django.utils.translation import gettext as _

from ..users.models import User
from ..middleware import get_current_user


class WorkplaceTypes(models.TextChoices):
    OUTPATIENT_TREATMENT = "OT", _("Outpatient treatment")  # Амбулаторный прием
    INPATIENT_TREATMENT = "IT", _("Inpatient treatment")  # Стационарное лечение
    CONSULTING_SERVICES = "CS", _("Consulting services")  # Консультирование


class WorkplaceProfile(models.TextChoices):
    # therapeutic
    THERAPEUTIC = "THER", _("Therapeutic")
    THERAPIST = "THER_TH", _("Therapist")
    NEUROLOGIST = "THER_NE", _("Neurologist")
    CARDIOLOGIST = "THER_CA", _("Сardiologist")

    # surgical
    SURGICAL = "SURG", _("Surgical")
    PHLEBOLOGIST = "SURG_PH", _("Phlebologist")

    # diagnostical
    DIAGNOSTICAL = "DIAG", _("Diagnostical")
    RADIOLOGIST = "DIAG_RA", _("Radiologist")
    ULTRASOUND = "DIAG_US", _("Ultrasound")


class Workplace(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    creator = models.ForeignKey(
        User, blank=False, default=get_current_user, on_delete=models.PROTECT,
        verbose_name=_('Workplace creator'),
    )
    name = models.CharField(
        max_length=255, unique=True, blank=False,
        verbose_name=_('Workplace name'),
    )
    type = models.CharField(
        max_length=2,
        choices=WorkplaceTypes,
        default=WorkplaceTypes.OUTPATIENT_TREATMENT,
        verbose_name=_('Workplace type'),
    )
    profile = models.CharField(
        max_length=7,
        choices=WorkplaceProfile,
        default=WorkplaceProfile.THERAPEUTIC,
        verbose_name=_('Workplace profile'),
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_type(self):
        match self.type:
            case 'OT':
                return WorkplaceTypes.OUTPATIENT_TREATMENT.label
            case 'IT':
                return WorkplaceTypes.INPATIENT_TREATMENT.label
            case 'CS':
                return WorkplaceTypes.CONSULTING_SERVICES.label

    def get_main_profile(self):
        profile = self.profile[:4]
        match profile:
            case 'THER':
                return WorkplaceProfile.THERAPEUTIC.label
            case 'SURG':
                return WorkplaceProfile.SURGICAL.label
            case 'DIAG':
                return WorkplaceProfile.DIAGNOSTICAL.label

    def get_sub_profile(self):
        if len(self.profile) > 4:
            subprofile = self.profile.split('_')[1]
            match subprofile:
                # therapeutic
                case 'TH':
                    return WorkplaceProfile.THERAPIST.label
                case 'NE':
                    return WorkplaceProfile.NEUROLOGIST.label
                case 'CA':
                    return WorkplaceProfile.CARDIOLOGIST.label
                # surgical
                case 'PH':
                    return WorkplaceProfile.PHLEBOLOGIST.label
                # diagnostical
                case 'RA':
                    return WorkplaceProfile.RADIOLOGIST.label
                case 'US':
                    return WorkplaceProfile.ULTRASOUND.label
        else:
            return ''
