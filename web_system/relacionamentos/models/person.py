from datetime import date, timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from relacionamentos.models import BaseModel
from django.db import models
from relacionamentos.validators.funcoes import validate_cpf


class Person(BaseModel):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            help_text=_("The name of the person"),
                            verbose_name= _("Name"))
    birthdate = models.DateField(verbose_name=_("Birthdate"),
                                 help_text='Insert your birthday here.')
    cpf= models.CharField(max_length=11,
                          validators=[MinLengthValidator(11), validate_cpf],
                          help_text=_("Insert your CPF Number without dots"),)

    def __str__(self):
        return self.name

    def clean(self):
        today = date.today()

        try:
            if self.birthdate > today.replace(year=today.year - 18):
                raise ValidationError({"Birthdate":
                                       _("You must be 18 years old.")},
                                     code="error1"
                                    )
        except ValueError:
            # TODO: deve ser tratado ainda o ano bissexto para poder usar e
            pass