from .base_model import BaseModel
from django.db import models

class Restaurante(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    valor = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2)
    tipo_refeicao = models.CharField('Tipo Refeicao', max_length=100)
    faixa_de_preco = models.FloatField(default=0.0)
    aceita_reserva = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.nome}'