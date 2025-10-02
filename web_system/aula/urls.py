from django.urls import path, include
import aula.views as views_funcoes

app_name = "aula"

urlpatterns = [
    path('funcao/saudacao', # rota
         views_funcoes.saudacao, #
         name='saudacao'), # opcional

]
