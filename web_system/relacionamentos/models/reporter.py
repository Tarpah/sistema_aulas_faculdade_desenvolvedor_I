from relacionamentos.validators import validate_cpf
from . import BaseModel
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Reporter(BaseModel):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            verbose_name="Reporter",
                            help_text=_("Reporter Name"))

    cpf = models.CharField(max_length=11,
                           validators=[MinLengthValidator(11), validate_cpf],
                           help_text=_("Insert your CPF Number without dots"),)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email")

    #objects = ReporterManager()

    def __str__(self):
        return self.name

    def clean(self):
        try:
            if self.name == "teste":
                raise ValidationError(
                    _("Nome não pode ser 'teste'.")
                )
        except ValueError:
            pass