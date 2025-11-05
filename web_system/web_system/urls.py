from django.contrib import admin
from django.urls import path, include
from web_system.views import index
from views import contato

urlpatterns = [
#rotas do contato
    path('funcao/contato', views.contato, name='function_contato'),
    #path('funcao/search/', views.busca, name='search_function'),
    path('', index, name='index'),
    path('relacionamentos/', include('relacionamentos.urls',  namespace="app"),),
    path('aula/', include('aula.urls'),),
    path('admin/', admin.site.urls),
]