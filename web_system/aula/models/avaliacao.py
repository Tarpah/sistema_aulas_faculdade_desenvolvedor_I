from .base_model import BaseModel
from django.db import models
from datetime import date

class Avaliacao(BaseModel):
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