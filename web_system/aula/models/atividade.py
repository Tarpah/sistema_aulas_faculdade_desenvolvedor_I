from .base_model import BaseModel
from django.db import models
from ..validators.funcoes import validate_par
from ..validators import CodValidator
from django.contrib import admin

class Atividade(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    valor = models.DecimalField(verbose_name='Valor',
                                max_digits=10,
                                decimal_places=2,
                                default=0.00,
                                help_text='Digite o valor da atração em reais R$.',)

    turno = models.CharField(max_length=8,
                             null=True,
                             blank=True) # null para o back e blank para o front

    nota = models.FloatField(default=0, validators=[validate_par])
    duracao = models.DurationField(null=True, blank=True)
    ingresso = models.BooleanField(default=False)
    informacoes = models.TextField(null=True, blank=True)
    guia = models.BooleanField(default=False)
    endereco = models.TextField(null=True, blank=True, validators=[CodValidator()])
    participantes = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.id} - {self.nome}'

class AtividadeAdmin(admin.ModelAdmin):  # <- Herda de ModelAdmin
    list_display = ('nome', 'valor', 'update_at')
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('nome',)
    list_filter = ('nome',)