from .base_model import baseModel
from django.db import models

class Atividade(baseModel):
    nome = models.CharField('Nome', max_length=100)