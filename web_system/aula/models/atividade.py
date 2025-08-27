from .base_model import baseModel
from django.db import models
from datetime import date


class Atividade(baseModel):
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

class Local(baseModel):
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

class Avaliacao(baseModel):
    titulo = models.CharField('Titulo', max_length=100, default='')
    data_avaliacao = models.DateField(default=date.today, verbose_name='Data da Avaliação') # provavelmente é redundante, pois auto_now_add faz isso sozinho
    data_visita = models.DateField(default=date.today, verbose_name='Data da Visita')
    comentario = models.TextField(null=True, blank=True, verbose_name='Comentário')
    nota = models.FloatField(default=0.0)
    acompanhantes = models.CharField(max_length=20,
                                    null=True,
                                    blank=True) # questionar o professor provavelmente publico_alvo é melhor
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id} - {self.titulo}'

class Restaurante(baseModel):
    nome = models.CharField('Nome', max_length=100)
    valor = models.DecimalField(verbose_name='Valor', max_digits=10, decimal_places=2)
    tipo_refeicao = models.CharField('Tipo Refeicao', max_length=100)
    faixa_de_preco = models.FloatField(default=0.0)
    aceita_reserva = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.nome}'
