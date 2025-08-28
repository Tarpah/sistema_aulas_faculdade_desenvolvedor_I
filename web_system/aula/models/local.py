from .base_model import BaseModel
from django.db import models


class Local(BaseModel):
    nome = models.CharField('Nome', max_length=100, default='')
    endereco = models.TextField(blank=False, default='', verbose_name='Endereço')
    nota = models.FloatField(default=0.0)
    horario_abertura = models.TimeField(null=True, blank=True, verbose_name='Horário de Abertura')
    horario_fechamento = models.TimeField(null=True, blank=True, verbose_name='Horário de Fechamento')
    informacoes = models.TextField(null=True, blank=True, verbose_name='Informações')
    ingresso = models.BooleanField(default=False, verbose_name='Ingresso')
    valor = models.DecimalField(verbose_name='Valor',
                                max_digits=10,
                                decimal_places=2,
                                default=0.00,
                                help_text='Digite o valor da atração em reais R$.')
    acessibilidade = models.BooleanField(default=False, verbose_name='Acessibilidade')
    classificacao = models.IntegerField(default=0, verbose_name='Classificação')
    contato = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'