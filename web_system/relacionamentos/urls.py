from django.urls import path

# import das views iniciais de exemplo
from relacionamentos.views import PrimeiraView, SaudacaoView, NomeView

# import das views com funções simples
import relacionamentos.views.estatisca as views_funcoes

# import das views com funções manipulando o Reporter
from relacionamentos.views.reporter import reporter_list_function, reporter_list_details_function,  \
reporter_delete_function, reporter_cpf_generator_function, reporter_create_function, reporter_update_function

# imports das views com classes manipulando o Reporter
from relacionamentos.views.reporter_classe import ReporterListView, ReporterDetailsView, ReporterCPFGeneratorView, \
    ReporterDeleteView, ReporterCreateView, ReporterUpdateView

# imports das views com generic manipulando o Reporter
from relacionamentos.views.reporter_generic import ReporterListViewGeneric, ReporterDetailsViewGeneric, \
    ReporterDeleteViewGeneric, ReporterCreateViewGeneric, ReporterUpdateViewGeneric

# deve ter o mesmo nome do namespace
app_name = 'relacionamentos'

urlpatterns = [

    # rotas do reporter com generic
    path('reporter/generic/update/<int:pk>', ReporterUpdateViewGeneric.as_view(), name='reporter_update_generic'),
    path('reporter/generic/create/', ReporterCreateViewGeneric.as_view(), name='reporter_create_generic'),
    path('reporter/generic/delete/<int:pk>', ReporterDeleteViewGeneric.as_view(), name='reporter_delete_generic'),
    path('reporter/generic/details/<int:pk>', ReporterDetailsViewGeneric.as_view(), name='reporter_details_generic'),
    path('reporter/generic/', ReporterListViewGeneric.as_view(), name='reporter_list_generic'),

    # rotas do reporter com classes
    path('reporter/class/update/<int:pk>', ReporterUpdateView.as_view(), name='reporter_update_class'),
    path('reporter/class/create/', ReporterCreateView.as_view(), name='reporter_create_class'),
    path('reporter/class/delete/<int:pk>', ReporterDeleteView.as_view(), name='reporter_delete_class'),
    path('reporter/class/cpf_generator/<int:pk>',  ReporterCPFGeneratorView.as_view(), name="reporter_cpf_generator_class"),
    path('reporter/class/details/<int:pk>', ReporterDetailsView.as_view(), name='reporter_details_class'),
    path('reporter/class/', ReporterListView.as_view(), name='reporter_list_class'),

    # rotas do reporter com funções
    path('reporter/function/update/<int:pk>', reporter_update_function, name='reporter_update_function'),
    path('reporter/function/create', reporter_create_function , name='reporter_create_function'),
    path('reporter/function/delete/<int:pk>', reporter_delete_function, name='reporter_delete_function'),
    path('reporter/function/cpf_generator/<int:pk>', reporter_cpf_generator_function, name='reporter_cpf_generator_function'),
    path('reporter/function/details/<int:pk>', reporter_list_details_function, name='reporter_list_details_function'),
    path('reporter/function/', reporter_list_function, name='reporter_list_function'),

    # rotas testes com classes
    path('home/', views_funcoes.home_view, name='home_view'),
    path('exemplo/classe/<str:name>', NomeView.as_view(), name='exemplo'),
    path('classe/teste', PrimeiraView.as_view(), name='primeira_view_classe'),

    # rotas exercicios para entendendimento de passagem de parametros na url
    path('funcao/exercicio/calculos/<int:x>/<int:y>', views_funcoes.calculos_basicos, name='calculos_basicos'),
    path('funcao/exercicio/<str:name>', views_funcoes.criptografia_senha, name='criptografia_senha'),

    # rotas básicas para entendimento
    path('funcao/teste', views_funcoes.primeira_view, name='primeira_view'),
    path('funcao/<str:name>', views_funcoes.nome, name='nome'),
    path('classe/saudacao', SaudacaoView.as_view(), name='saudacao_view_classe'),
]

