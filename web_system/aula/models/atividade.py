from .base_model import BaseModel
from django.db import models
from datetime import date


class Atividade(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    valor = models.DecimalField(verbose_name='Valor',
                                max_digits=10,
                                decimal_places=2,
                                default=0.00,
                                help_text='Digite o valor da atração em reais R$.')

    turno = models.CharField(max_length=8,
                             null=True,
                             blank=True) # null para o back e blank para o front

    nota = models.FloatField(default=0.0)
    duracao = models.DurationField(null=True, blank=True)
    ingresso = models.BooleanField(default=False)
    informacoes = models.TextField(null=True, blank=True)
    guia = models.BooleanField(default=False)
    endereco = models.TextField(null=True, blank=True)
    participantes = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id} - {self.nome}'
