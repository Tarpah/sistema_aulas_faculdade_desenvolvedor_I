from django.contrib import admin
from aula.models import Atividade, Restaurante, Local, Avaliacao


# Register your models here.
admin.site.register(Atividade)
admin.site.register(Avaliacao)
admin.site.register(Restaurante)
admin.site.register(Local)
