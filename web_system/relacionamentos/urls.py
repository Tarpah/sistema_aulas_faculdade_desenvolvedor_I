from django.urls import path

# import das views iniciais de exemplo
from relacionamentos.views import PrimeiraView, SaudacaoView, NomeView

# import das views com funções simples
import relacionamentos.views.estatisca as views_funcoes

# import das views com funções manipulando o Reporter
from relacionamentos.views.reporter import function_reporter_list, reporter_list_details, delete, gerar_cpf_function, create, update

# imports das views com classes manipulando o Reporter
from relacionamentos.views.reporter_classe import ReporterListClasse, ReporterListDetailsClasse, ReporterGerarCPF, \
    ReporterDeleteView, ReporterCreateView


# deve ter o mesmo nome do namespace
app_name = 'relacionamentos'

urlpatterns = [

    # rotas do reporter com classes
    path('reporter/class/criar/', ReporterCreateView.as_view(), name='reporter_class_create'),
    path('reporter/class/delete/<int:pk>', ReporterDeleteView.as_view(), name='reporter_class_delete'),
    path('reporter/classe/gerar_cpf/<int:pk>',  ReporterGerarCPF.as_view(), name="gerar_cpf_classe"),
    path('reporter/classe/read/<int:pk>', ReporterListDetailsClasse.as_view(), name='reporter_classe_read'),
    path('reporter/classe/', ReporterListClasse.as_view(), name='reporter_class_read'),

    # rotas do reporter com funções
    path('reporter/funcao/update/<int:pk>', update, name='reporter_function_update'),
    path('reporter/funcao/create', create , name='reporter_function_create'),
    path('reporter/funcao/gerar_cpf_function/<int:pk>', gerar_cpf_function, name='gerar_cpf_function'),
    path('reporter/funcao/delete/<int:pk>', delete, name='reporter_function_delete'),
    path('reporter/funcao/read/<int:pk>', reporter_list_details, name='reporter_function_read'),
    path('reporter/funcao/', function_reporter_list, name='reporter_function_list'),
    path('home/', views_funcoes.home_view, name='home_view'),

    # rotas testes com classes
    path('exemplo/classe/<str:name>', NomeView.as_view(), name='exemplo'),
    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),

    # rotas exercicios
    path('funcao/exercicio/calculos/<int:x>/<int:y>', views_funcoes.calculos_basicos, name='calculos_basicos'),
    path('funcao/exercicio/<str:name>', views_funcoes.criptografia_senha, name='criptografia_senha'),

    # rotas básicas para entender
    path('funcao/teste', views_funcoes.primeira_view, name='primeira_view'),
    path('funcao/<str:name>', views_funcoes.nome, name='nome'),
    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_view_classe'),
]

