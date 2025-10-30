from .base_model import BaseModel
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .magazine import Magazine
from .reporter import Reporter
from datetime import date

class Paper(BaseModel):
    title = models.CharField(max_length=100,
                              verbose_name='Titulo')
    pub_date = models.DateField(verbose_name='Data de publicação')
    reporter = models.ForeignKey(Reporter,
                                 on_delete=models.CASCADE,
                                 verbose_name='Reporter')

    magazines = models.ManyToManyField(Magazine, blank=True,
                                       through="Publication",
                                       through_fields=("paper", "magazine"))

    def __str__(self):
        return f"{self.title} by {self.reporter.name}"

    def clean(self):
        today = date.today()

        if self.pub_date < today:
            raise ValidationError(
                    _("Impossível publicar antes da data de hoje.")
            )