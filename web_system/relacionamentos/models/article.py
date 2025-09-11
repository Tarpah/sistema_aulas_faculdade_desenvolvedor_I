from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .magazine import Magazine
from .reporter import Reporter
from datetime import date

class Article(BaseModel):
    titulo = models.CharField(max_length=100,
                              verbose_name='Titulo')
    data_publicacao = models.DateField(verbose_name='Data de publicação')
    reporter = models.ForeignKey(Reporter,
                                 on_delete=models.RESTRICT,
                                 verbose_name='Reporter')
    magazines = models.ManyToManyField(Magazine)

    def __str__(self):
        return f"{self.titulo} por {self.reporter.name}"

    def clean(self):
        hoje = date.today()

        if self.data_publicacao < hoje:
            raise ValidationError(
                    _("Impossível publicar antes da data de hoje.")
            )