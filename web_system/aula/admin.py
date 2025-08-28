from django.contrib import admin
from aula.models import Atividade, Restaurante, Local, Avaliacao, Perfil


class AtividadeAdmin(admin.ModelAdmin):  # <- Herda de ModelAdmin
    list_display = ('nome', 'valor', 'update_at')
    readonly_fields = ('create_at', 'update_at')
    search_fields = ('nome',)
    list_filter = ('nome',)

# Register your models here.
admin.site.register((Avaliacao, Restaurante, Local, Perfil))
admin.site.register(Atividade,AtividadeAdmin)

