from .base_model import baseModel
from django.db import models

class Atividade(baseModel):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField(verbose_name='Preço',
                                max_digits=10,
                                decimal_places=2,
                                default=0.00,
                                help_text='Digite o valor da atração em reais R$.')

    turno = models.CharField(max_length=8,
                             null=True,
                             blank=True) # null para o back e blank para o front

    nota = models.FloatField(default=0.0)

    # nome: String{100}
    # turno: String{8}
    # nota: float
    # duracao: time
    # ingresso: bool
    # valor: decimal {opcional}
    # informações: String {text}
    # guia: bool
    # endereço: String
    # participantes: int

    def __str__(self):
        return f'{self.id} - {self.nome}'


class Local(baseModel):
    pass
    # nome: String {100}
    # endereco: String {200}
    # nota: float
    # horario_abertura: time
    # horario-fechamento: time
    # informacoes: String{text}
    # ingresso: bool
    # valor: decimal(opcional)
    # acessibilidade: bool
    # classificacao: int
    # contato: email


class Avaliacao(baseModel):
    pass
    # titulo: String {100}
    # data_avaliacao: date
    # data_visita: date
    # comentario: String {text}
    # nota: int
    # acompanhantes: String{20}
    # likes: int

