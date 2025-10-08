from django.urls import path, include
import relacionamentos.views.estatisca as views_funcoes
from relacionamentos.views import PrimeiraView
from relacionamentos.views import SaudacaoView
from relacionamentos.views import NomeView

# mesma coisa que namespace
app_name = 'relacionamentos'


urlpatterns = [
    path('exemplo/classe/', NomeView.as_view(), name='exemplo'),
    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),
    path('funcao/exercicio/calculos/<int:x>/<int:y>', views_funcoes.calculos_basicos, name='calculos_basicos'),
    path('funcao/exercicio/<str:name>', views_funcoes.criptografia_senha, name='criptografia_senha'),
    path('funcao/teste', views_funcoes.primeira_view, name='primeira_view'),
    path('funcao/<str:name>', views_funcoes.nome, name='nome'),
    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_view'),
]

