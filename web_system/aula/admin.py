from django.contrib import admin
from aula.models import Atividade, Restaurante, Local, Avaliacao, Perfil, Tag


# Register your models here.
admin.site.register((Atividade, Avaliacao, Restaurante, Local, Perfil, Tag))
