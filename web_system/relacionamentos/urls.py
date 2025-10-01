from django.urls import path, include
import relacionamentos.views as views_funcoes

# mesma coisa que namespace
app_name = 'relacionamentos'


urlpatterns = [
    path('funcao/teste', views_funcoes.primeira_view,
         name='primeira_view'),
]
