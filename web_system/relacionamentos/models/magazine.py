from .base_model import BaseModel
from django.db import models

class Magazine(BaseModel):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    edicao = models.CharField(max_length=100, verbose_name='Edição')

    def __str__(self):
        return f"{self.nome}"
