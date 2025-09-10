from relacionamentos.validators import validate_cpf
from . import BaseModel
from django.db import models


class Reporter(BaseModel):
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)],
                            verbose_name="Reporter",
                            help_text=("Reporter Name"))

    cpf = models.CharField(max_length=11,
                           validators=[MinLengthValidator(11), validate_cpf],
                           help_text=("Insert your CPF Number without dots"),)
    email = models.EmailField(max_length=255,)

    #objects = ReporterManager()

    def __str__(self):
        return self.name
