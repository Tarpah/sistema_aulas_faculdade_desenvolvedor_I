from random import choices

from web_system.aula.enumerate import Genero
from web_system.aula.models import baseModel
from django.db import models

class Perfil(baseModel):
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', help_text='Data de Nascimento')
    bio = models.TextField(verbose_name='Biografia', null=True, blank=True, default='', max_length=255)
    passaporte = models.TextField(max_length=255, verbose_name='Passaporte', null=True, blank=True)
    cidade = models.TextField(max_length=255, verbose_name='Cidade', null=True, blank=True)
    pais = models.TextField()
    genero = models.CharField(max_length=20,
                              choices=Genero,
                              default=Genero.NOT_SPECIFIED)


    # Data_Nascimento: Date
    # bio = String(255)
    # passaporte: String{10}
    # genero: Genero(classe)
    # cidade: String(255)
    # pais: String(60)