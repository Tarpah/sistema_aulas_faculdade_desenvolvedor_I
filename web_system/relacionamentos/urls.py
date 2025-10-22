from django.urls import path, include
import relacionamentos.views.estatisca as views_funcoes
from relacionamentos.views import PrimeiraView, SaudacaoView, NomeView
from relacionamentos.views.reporter import reporter_list, reporter_list_details, delete, gerar_cpf

# mesma coisa que namespace
app_name = 'relacionamentos'

urlpatterns = [
    path('reporter/funcao/gerar_cpf/<int:pk>', gerar_cpf, name='gerar_cpf'),
    path('reporter/funcao/delete/<int:pk>', delete, name='reporter_function_delete'),
    path('reporter/funcao/read/<int:pk>', reporter_list_details, name='exemplo_function_read'),
    path('reporter/funcao/', reporter_list, name='exemplo_function_list'),
    path('home/', views_funcoes.home_view, name='home_view'),
    path('exemplo/classe/<str:name>', NomeView.as_view(), name='exemplo'),
    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),
    path('funcao/exercicio/calculos/<int:x>/<int:y>', views_funcoes.calculos_basicos, name='calculos_basicos'),
    path('funcao/exercicio/<str:name>', views_funcoes.criptografia_senha, name='criptografia_senha'),
    path('funcao/teste', views_funcoes.primeira_view, name='primeira_view'),
    path('funcao/<str:name>', views_funcoes.nome, name='nome'),
    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_view_classe'),
]

