from random import choices

from ..enumerate import Genero
from . import BaseModel
from django.db import models

class Perfil(BaseModel):
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', help_text='Data de Nascimento')
    bio = models.TextField(verbose_name='Biografia', null=True, blank=True, default='', max_length=255)
    passaporte = models.TextField(max_length=255, verbose_name='Passaporte')
    cidade = models.TextField(max_length=255, verbose_name='Cidade', null=True, blank=True)
    pais = models.TextField(max_length=60, verbose_name='Pais')
    genero = models.CharField(max_length=20,
                              choices=Genero,
                              default=Genero.NOT_SPECIFIED)


    # Data_Nascimento: Date
    # bio = String(255)
    # passaporte: String{10}
    # genero: Genero(classe)
    # cidade: String(255)
    # pais: String(60)

    def __str__(self):
        return f'{self.id} - {self.passaporte}'