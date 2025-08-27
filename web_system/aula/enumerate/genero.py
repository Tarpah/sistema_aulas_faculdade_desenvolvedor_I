from django.db import models
from django.utils.translation import gettext_lazy as _


class Genero(models.TextChoices):
    MALE = 'MALE', _('Masculino')
    FEMALE = 'FEMALE', _('Feminino')
    OTHER = 'OTHER', _('Outro')
    NOT_SPECIFIED = 'NOT SPECIFIED', _('Não especificado')