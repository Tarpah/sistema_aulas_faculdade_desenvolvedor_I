from django.contrib import admin
from aula.models import Atividade, AtividadeAdmin, Restaurante, Local, Avaliacao, Perfil, Tag

# Register your models here.
admin.site.register((Avaliacao, Restaurante, Local, Perfil, Tag))
admin.site.register(Atividade,AtividadeAdmin)
